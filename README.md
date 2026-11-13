# Arme P&B — dieta e palestra in un'unica app

- `index.html`: shell con login Firebase e sincronizzazione dei dati tra dispositivi
- `diet/`: piano alimentare adattivo (sorgenti in `diet/src`, `python3 build.py` dentro `diet/`)
- `gym/`: scheda palestra A/B/C con schema muscolare
- `config.js`: configurazione web pubblica di Firebase
- `firestore.rules`: regole Firestore (ogni utente vede solo i suoi dati, `users/{uid}/state/{diet,gym}`)

Netlify: branch `main`, nessun build command, publish directory `/`.

## Crediti
Lo schema muscolare usa i poligoni di [react-body-highlighter](https://github.com/giavinh79/react-body-highlighter) (MIT, © GV79).
