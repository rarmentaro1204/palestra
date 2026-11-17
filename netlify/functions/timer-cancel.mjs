// Ferma una notifica di recupero già programmata (cronometro saltato o cambiato).
import { getStore } from '@netlify/blobs';

export default async (req) => {
  try {
    const { id } = await req.json();
    if (id) await getStore({ name: 'timer', consistency: 'strong' }).set(String(id).slice(0, 64), '1');
  } catch (e) {}
  return new Response('ok');
};

export const config = { path: '/api/timer-cancel' };
