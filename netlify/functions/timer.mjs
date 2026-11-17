// Notifica di fine recupero: aspetta i secondi del cronometro e poi manda una notifica push al telefono.
// Funzione in background (fino a 15 minuti). Se nel frattempo il cronometro viene fermato, timer-cancel segna l'id e qui non si manda niente.
import webpush from 'web-push';
import { getStore } from '@netlify/blobs';

const clip = (s, n) => String(s || '').slice(0, n);

export default async (req) => {
  try {
    const { sub, id, ms, title, body } = await req.json();
    if (!sub || typeof sub.endpoint !== 'string' || !/^https:\/\//.test(sub.endpoint) || !id) return;
    const wait = Math.max(0, Math.min(Number(ms) || 0, 14 * 60 * 1000));
    await new Promise((r) => setTimeout(r, wait));
    try {
      const store = getStore({ name: 'timer', consistency: 'strong' });
      if (await store.get(String(id))) { await store.delete(String(id)); return; }
    } catch (e) { console.log('controllo annullamento non riuscito', e && e.message); }
    webpush.setVapidDetails('https://palestraarme.netlify.app', process.env.VAPID_PUBLIC, process.env.VAPID_PRIVATE);
    await webpush.sendNotification(sub, JSON.stringify({ title: clip(title, 60) || '⏱ Recupero finito', body: clip(body, 140), tag: 'timer' }), { TTL: 60, urgency: 'high' });
  } catch (e) {
    // niente rilanci: un nuovo tentativo arriverebbe in ritardo
    console.log('timer push non inviata', e && (e.statusCode || e.message));
  }
};

export const config = { background: true, path: '/api/timer' };
