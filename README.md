# Arme P&B — dieta e palestra in un'unica app

- `index.html`: cornice dell'app (barra Oggi · Allenamento · Piano · Spesa · Progressi), login Firebase e sincronizzazione dei dati tra dispositivi
- `diet/`: piano alimentare adattivo con registro pasti (sorgenti in `diet/src`, tabella alimenti in `diet/src/foods.py`; `python3 build.py` dentro `diet/`)
- `gym/`: scheda palestra A/B/C con schema muscolare
- `config.js`: configurazione web pubblica di Firebase
- `firestore.rules`: regole Firestore (ogni utente vede solo i suoi dati, `users/{uid}/state/{diet,gym}`)

Netlify: branch `main`, nessun build command, publish directory `/`.

## Crediti
Lo schema muscolare usa i poligoni di [react-body-highlighter](https://github.com/giavinh79/react-body-highlighter) (MIT, © GV79).
Le foto degli esercizi nuovi (chest press, panca inclinata manubri, rotazioni esterne, Pallof press, pulley, farmer walk) vengono da [free-exercise-db](https://github.com/yuhonas/free-exercise-db) (Unlicense, pubblico dominio).

## Notifiche del cronometro

- `sw.js` (service worker) mostra la notifica; `manifest.webmanifest` e le icone permettono di aggiungere l'app alla schermata Home (su iPhone le notifiche web funzionano solo così).
- `netlify/functions/timer.mjs` è una funzione in background senza dipendenze: riceve la subscription e i secondi del recupero, aspetta, controlla su Firestore (documento `gym`, campo `timer`) che il cronometro non sia stato saltato o cambiato e manda la push (Web Push cifrata aes128gcm + VAPID, solo `node:crypto`).
- Variabili d'ambiente su Netlify: `VAPID_PUBLIC`, `VAPID_PRIVATE` (segreta).

## Ricette

`diet/src/ricette.py` genera `ric.json` (109 ricette). Le idee vengono da GialloZafferano, dai blog di GialloZafferano e da Fatto in casa da Benedetta: non copiamo testi né foto, le dosi sono quelle del piano e i passaggi sono riscritti in versione leggera; ogni ricetta ha il link all'originale (`src`).
