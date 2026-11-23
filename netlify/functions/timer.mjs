// Notifica di fine recupero, senza librerie esterne (solo Node).
// La pagina manda: subscription push, id del cronometro, millisecondi, uid e token Firebase.
// La funzione aspetta, poi controlla su Firestore che il cronometro non sia stato annullato
// (se lo salti o lo cambi, la pagina scrive subito il suo id nel campo "cancel" del documento "gym") e manda la push.
import crypto from 'node:crypto';

const PROJECT = 'sitoberto-85f50';
const SUBJECT = 'https://palestraarme.netlify.app';
const b64u = (b) => Buffer.from(b).toString('base64url');
const clip = (s, n) => String(s || '').slice(0, n);

function vapidJWT(aud) {
  const pub = Buffer.from(process.env.VAPID_PUBLIC, 'base64url');
  const key = crypto.createPrivateKey({ format: 'jwk', key: { kty: 'EC', crv: 'P-256', x: b64u(pub.subarray(1, 33)), y: b64u(pub.subarray(33, 65)), d: process.env.VAPID_PRIVATE } });
  const head = b64u(JSON.stringify({ typ: 'JWT', alg: 'ES256' }));
  const body = b64u(JSON.stringify({ aud, exp: Math.floor(Date.now() / 1000) + 12 * 3600, sub: SUBJECT }));
  const sig = crypto.sign('sha256', Buffer.from(head + '.' + body), { key, dsaEncoding: 'ieee-p1363' });
  return head + '.' + body + '.' + b64u(sig);
}

// RFC 8291 (aes128gcm)
export function encrypt(sub, text) {
  const ua = Buffer.from(sub.keys.p256dh, 'base64url'), auth = Buffer.from(sub.keys.auth, 'base64url');
  const ecdh = crypto.createECDH('prime256v1'); ecdh.generateKeys();
  const as = ecdh.getPublicKey(), shared = ecdh.computeSecret(ua), salt = crypto.randomBytes(16);
  const hk = (s, ikm, info, n) => Buffer.from(crypto.hkdfSync('sha256', ikm, s, info, n));
  const ikm = hk(auth, shared, Buffer.concat([Buffer.from('WebPush: info\0'), ua, as]), 32);
  const cek = hk(salt, ikm, Buffer.from('Content-Encoding: aes128gcm\0'), 16);
  const nonce = hk(salt, ikm, Buffer.from('Content-Encoding: nonce\0'), 12);
  const c = crypto.createCipheriv('aes-128-gcm', cek, nonce);
  const ct = Buffer.concat([c.update(Buffer.concat([Buffer.from(text), Buffer.from([2])])), c.final(), c.getAuthTag()]);
  const rs = Buffer.alloc(4); rs.writeUInt32BE(4096);
  return Buffer.concat([salt, rs, Buffer.from([as.length]), as, ct]);
}

export async function sendPush(sub, text) {
  const aud = new URL(sub.endpoint).origin;
  const r = await fetch(sub.endpoint, { method: 'POST', body: encrypt(sub, text), headers: {
    TTL: '60', Urgency: 'high', 'Content-Encoding': 'aes128gcm', 'Content-Type': 'application/octet-stream',
    Authorization: 'vapid t=' + vapidJWT(aud) + ', k=' + process.env.VAPID_PUBLIC } });
  return r.status;
}

async function stillActive(uid, token, id) {
  if (!uid || !token) return true;
  try {
    const u = `https://firestore.googleapis.com/v1/projects/${PROJECT}/databases/(default)/documents/users/${encodeURIComponent(uid)}/state/gym`;
    const r = await fetch(u, { headers: { Authorization: 'Bearer ' + token } });
    if (!r.ok) return true;
    const doc = await r.json(), c = doc.fields && doc.fields.cancel && doc.fields.cancel.stringValue;
    return c !== id;
  } catch (e) { return true; }
}

export default async (req) => {
  try {
    const { sub, id, ms, uid, token, title, body } = await req.json();
    if (!sub || typeof sub.endpoint !== 'string' || !/^https:\/\//.test(sub.endpoint) || !sub.keys || !id) return;
    const wait = Math.max(0, Math.min(Number(ms) || 0, 14 * 60 * 1000));
    await new Promise((r) => setTimeout(r, wait));
    if (!(await stillActive(uid, token, id))) return;
    const st = await sendPush(sub, JSON.stringify({ title: clip(title, 60) || '⏱ Recupero finito', body: clip(body, 140), tag: 'timer-' + clip(id, 20) }));
    if (st >= 300) console.log('push rifiutata', st);
  } catch (e) {
    console.log('timer push non inviata', e && e.message);
  }
};

export const config = { background: true, path: '/api/timer' };
