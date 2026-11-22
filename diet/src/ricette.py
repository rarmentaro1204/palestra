# Ricette (nov 2026): ispirate a GialloZafferano, ai blog di GialloZafferano e a Fatto in casa da Benedetta.
# Non copiamo testi né foto: titolo dell'idea, quantità rifatte sulle dosi del piano, passaggi scritti da noi
# in versione leggera, e il link alla ricetta originale per foto e procedimento completo.
# Quantità: "R:190g F:140g" = Berto / Pesca; "200g+150g" = Berto + Pesca.
# Regole: niente pesce per Berto, niente cavolfiori, carne rossa solo negli slot cenCar e praRagu.
import json

GZ, GZB, BEN = 'GialloZafferano', 'Blog GialloZafferano', 'Fatto in casa da Benedetta'
R = []


def add(slot, p, e, n, mins, ing, steps, src, srcN, note='', we=False):
    R.append({'id': '%s%02d' % (slot, sum(1 for x in R if x['slot'] == slot) + 1), 'slot': slot, 'p': p, 'we': we, 'e': e, 'n': n,
              'min': mins, 'ing': ing, 'steps': steps, 'note': note, 'src': src, 'srcN': srcN})


# ---------- COLAZIONE BERTO (porridge caldo, niente proteine in polvere) ----------
LAT, AV = ['Latte scremato', '200 ml'], ["Fiocchi d'avena", '40 g']
add('colR', 'R', '🍫', 'Porridge al cioccolato fondente', 7, [LAT, AV, ['Cioccolato fondente', '10 g'], ['Cannella', 'q.b.']],
    ['Scalda latte e avena a fuoco basso, mescolando, per 4-5 minuti.', 'Spegni, aggiungi il cioccolato a pezzetti e lascia sciogliere.', 'Spolvera di cannella.'],
    'https://www.fattoincasadabenedetta.it/ricetta/porridge/', BEN, 'La base del piano.')
add('colR', 'R', '🍎', 'Porridge mela e cannella', 8, [LAT, AV, ['Mela a dadini', '80 g'], ['Cannella', '½ cucchiaino']],
    ['Cuoci la mela 2 minuti in padellino con un goccio d’acqua e la cannella.', 'Aggiungi latte e avena e cuoci 4-5 minuti.', 'Servi con la mela sopra.'],
    'https://ricette.giallozafferano.it/Porridge.html', GZ)
add('colR', 'R', '🍌', 'Porridge banana e cacao', 7, [LAT, AV, ['Banana', '50 g'], ['Cacao amaro', '5 g']],
    ['Schiaccia metà banana nel latte e porta a bollore con l’avena.', 'A fine cottura aggiungi il cacao.', 'Completa con l’altra metà a rondelle.'],
    'https://blog.giallozafferano.it/dulcisinforno/porridge-ricetta-avena/', GZB)
add('colR', 'R', '🍐', 'Porridge pera e noci', 8, [LAT, AV, ['Pera', '80 g'], ['Noci', '5 g']],
    ['Cuoci latte e avena con la pera grattugiata, così si addolcisce senza zucchero.', 'Servi con le noci tritate.'],
    'https://blog.giallozafferano.it/rusyna/porridge-di-avena/', GZB)
add('colR', 'R', '🎃', 'Porridge alla zucca speziata', 10, [LAT, AV, ['Zucca cotta (anche avanzata)', '60 g'], ['Miele', '5 g'], ['Cannella e zenzero', 'q.b.']],
    ['Frulla o schiaccia la zucca cotta.', 'Cuoci con latte, avena e spezie per 5 minuti.', 'Un filo di miele alla fine.'],
    'https://blog.giallozafferano.it/atavolacontea/ricetta-porridge-overnight-oats-autunnale/', GZB, 'Versione calda dell’idea autunnale del blog.')
add('colR', 'R', '🫐', 'Porridge ai frutti di bosco caldi', 8, [LAT, AV, ['Frutti di bosco surgelati', '80 g'], ['Miele', '4 g']],
    ['Scalda i frutti di bosco 3 minuti finché fanno il loro sugo.', 'Cuoci latte e avena a parte.', 'Versa la composta calda sopra.'],
    'https://www.fattoincasadabenedetta.it/ricetta/overnight-porridge/', BEN)
add('colR', 'R', '🥜', 'Porridge burro d’arachidi e banana', 7, [LAT, AV, ['Burro d’arachidi', '7 g'], ['Banana', '40 g']],
    ['Cuoci latte e avena 4-5 minuti.', 'Spegni e sciogli dentro il burro d’arachidi.', 'Banana a rondelle sopra.'],
    'https://blog.giallozafferano.it/studentiaifornelli/ricetta-3-idee-di-porridge-overnight-senza-cottura/', GZB)
add('colR', 'R', '🥞', 'Pancake d’avena e banana', 12, [AV, ['Latte scremato', '100 ml'], ['Albume', '60 g'], ['Banana', '50 g'], ['Cannella', 'q.b.']],
    ['Frulla avena, latte, albume e banana.', 'Cuoci a cucchiaiate in padella antiaderente, 1-2 minuti per lato.', 'Bevi il latte rimasto (100 ml) caldo.'],
    'https://blog.giallozafferano.it/ricettepanedolci/pancake-farina-avena-e-yogurt/', GZB, 'Senza proteine in polvere: le proteine arrivano dall’albume.', we=True)

# ---------- COLAZIONE PESCA ----------
AVF, LIF, FS = ["Fiocchi d'avena", '30 g'], ['Latte intero', '150 ml'], ['Frutta secca', '8 g']
add('colF', 'F', '🍎', 'Porridge mela e cannella', 8, [AVF, LIF, ['Mela', '100 g'], FS, ['Cannella', 'q.b.']],
    ['Cuoci latte e avena 4 minuti.', 'Aggiungi la mela a dadini e la cannella, 1 minuto ancora.', 'Frutta secca tritata sopra.'],
    'https://ricette.giallozafferano.it/Porridge.html', GZ)
add('colF', 'F', '🍐', 'Porridge pera e cioccolato', 8, [AVF, LIF, ['Pera', '100 g'], ['Cioccolato fondente', '8 g']],
    ['Cuoci latte e avena con la pera a pezzetti.', 'Spegni e aggiungi il cioccolato a scaglie.'],
    'https://www.fattoincasadabenedetta.it/ricetta/porridge/', BEN)
add('colF', 'F', '🥣', 'Overnight oats alla mela', 5, [AVF, LIF, ['Mela grattugiata', '100 g'], FS, ['Cannella', 'q.b.']],
    ['La sera mescola tutto in un barattolo e metti in frigo.', 'La mattina scalda 1 minuto al microonde se lo vuoi tiepido.'],
    'https://ricette.giallozafferano.it/Porridge-overnight.html', GZ)
add('colF', 'F', '🍊', 'Porridge all’arancia e mandorle', 8, [AVF, LIF, ['Arancia a spicchi', '100 g'], ['Mandorle a lamelle', '8 g'], ['Scorza d’arancia', 'q.b.']],
    ['Cuoci latte e avena con un po’ di scorza grattugiata.', 'Servi con spicchi d’arancia e mandorle.'],
    'https://blog.giallozafferano.it/valeriaciccotti/porridge/', GZB)
add('colF', 'F', '🥞', 'Pancake d’avena e frutta', 12, [["Farina d'avena", '25 g'], ['Uovo', '1'], ['Latte intero', '60 ml'], ['Frutta di stagione', '100 g'], ['Miele', '6 g']],
    ['Mescola farina, uovo e latte.', 'Cuoci 3-4 pancake in padella antiaderente.', 'Frutta e un filo di miele sopra.'],
    'https://blog.giallozafferano.it/neltegamesulfuoco/pancake-di-avena/', GZB, we=True)
add('colF', 'F', '🍫', 'Porridge cacao e banana', 7, [AVF, LIF, ['Banana', '80 g'], ['Cacao amaro', '5 g']],
    ['Cuoci latte e avena con metà banana schiacciata.', 'Aggiungi il cacao e il resto della banana.'],
    'https://blog.giallozafferano.it/dulcisinforno/porridge-ricetta-avena/', GZB)
add('colF', 'F', '🎃', 'Porridge zucca e cannella', 10, [AVF, LIF, ['Zucca cotta', '80 g'], ['Miele', '5 g'], ['Cannella', 'q.b.']],
    ['Schiaccia la zucca e cuocila con latte e avena.', 'Miele e cannella alla fine.'],
    'https://blog.giallozafferano.it/atavolacontea/ricetta-porridge-overnight-oats-autunnale/', GZB)
add('colF', 'F', '🥚', 'Porridge cremoso con l’uovo', 8, [["Farina d'avena", '20 g'], ['Uovo', '1'], LIF, ['Miele', '8 g'], ['Frutta di stagione', '100 g']],
    ['Cuoci latte e farina d’avena 3 minuti.', 'Fuori dal fuoco sbatti dentro l’uovo velocemente: diventa una crema.', 'Rimetti 30 secondi sul fuoco, poi miele e frutta.'],
    'https://www.fattoincasadabenedetta.it/ricetta/porridge/', BEN, 'È la colazione “B” del piano.')

# ---------- PRANZO BERTO: PASTA E CARNE BIANCA ----------
PI, TA, OL = ['Pasta integrale', '70 g'], ['Petto di tacchino o pollo', '130 g'], ['Olio EVO', '5 ml']
add('praPasta', 'R', '🍋', 'Pasta, tacchino e zucchine al limone', 20, [PI, ['Straccetti di tacchino', '130 g'], OL, ['Zucchine', '200 g'], ['Limone (scorza e succo)', '½']],
    ['Rosola gli straccetti 4-5 minuti, sfuma con il limone.', 'Aggiungi le zucchine a julienne per 4 minuti.', 'Salta la pasta nel condimento con la scorza grattugiata.'],
    'https://www.fattoincasadabenedetta.it/ricetta/straccetti-di-tacchino/', BEN)
add('praPasta', 'R', '🍄', 'Pasta pollo e funghi', 20, [PI, TA, OL, ['Funghi champignon', '200 g'], ['Aglio e prezzemolo', 'q.b.']],
    ['Trifola i funghi con aglio e un mestolo d’acqua.', 'Aggiungi il pollo a cubetti e cuoci 6 minuti.', 'Manteca la pasta con un po’ d’acqua di cottura e prezzemolo.'],
    'https://www.fattoincasadabenedetta.it/ricetta/petto-di-pollo-con-funghi/', BEN)
add('praPasta', 'R', '🎃', 'Pasta zucca, pollo e rosmarino', 25, [PI, TA, OL, ['Zucca', '200 g'], ['Rosmarino', 'q.b.']],
    ['Cuoci la zucca a dadini con acqua e rosmarino finché è cremosa.', 'Rosola il pollo a parte.', 'Unisci pasta, crema di zucca e pollo.'],
    'https://ricette.giallozafferano.it/Pasta-con-la-zucca.html', GZ)
add('praPasta', 'R', '🥦', 'Pasta broccoli e straccetti di pollo', 20, [PI, TA, OL, ['Broccoli (cime)', '200 g'], ['Peperoncino', 'q.b.']],
    ['Cuoci i broccoli nell’acqua della pasta.', 'Salta pollo, aglio e peperoncino in padella.', 'Unisci pasta e broccoli e schiaccia qualche cima per fare crema.'],
    'https://ricette.giallozafferano.it/Pasta-con-broccoli.html', GZ)
add('praPasta', 'R', '🤍', 'Pasta al ragù bianco di tacchino', 30, [PI, ['Macinato di tacchino', '130 g'], OL, ['Carota, sedano, cipolla', '200 g'], ['Vino bianco', 'un goccio'], ['Rosmarino', 'q.b.']],
    ['Soffriggi le verdure tritate con l’olio e un goccio d’acqua.', 'Rosola il macinato, sfuma col vino e cuoci 15 minuti.', 'Condisci la pasta.'],
    'https://ricette.giallozafferano.it/Tagliatelle-al-ragu-bianco.html', GZ, 'Versione col tacchino al posto di manzo e maiale.')
add('praPasta', 'R', '🍅', 'Pasta pollo, pomodorini e rucola al balsamico', 20, [PI, TA, OL, ['Pomodorini', '150 g'], ['Rucola', '50 g'], ['Aceto balsamico', '1 cucchiaio']],
    ['Rosola gli straccetti e sfuma col balsamico.', 'Aggiungi i pomodorini tagliati per 3 minuti.', 'Pasta, condimento e rucola a crudo.'],
    'https://blog.giallozafferano.it/pelledipollo/straccetti-di-pollo-al-balsamico-con-rucola-pomodori/', GZB)
add('praPasta', 'R', '🥬', 'Pasta radicchio e tacchino', 20, [PI, TA, OL, ['Radicchio', '200 g'], ['Cipolla', '½']],
    ['Appassisci cipolla e radicchio con un mestolo d’acqua.', 'Aggiungi il tacchino a dadini, 6 minuti.', 'Manteca la pasta.'],
    'https://ricette.giallozafferano.it/Pasta-radicchio-e-zola.html', GZ, 'Senza gorgonzola, con il tacchino.')

# ---------- PRANZO BERTO: RISO E POLLO ----------
RI, PO, PIS, ZU = ['Riso (basmati o integrale)', '70 g'], ['Petto di pollo', '130 g'], ['Piselli', '100 g'], ['Zucchine', '100 g']
add('praRiso', 'R', '🎃', 'Risotto zucca e pollo', 30, [['Riso Carnaroli', '70 g'], PO, OL, ['Zucca', '150 g'], ['Brodo vegetale', '400 ml']],
    ['Cuoci la zucca a dadini con il riso, aggiungendo brodo un mestolo alla volta.', 'Rosola il pollo a parte.', 'Unisci a fine cottura.'],
    'https://ricette.giallozafferano.it/Risotto-zucca-e-funghi.html', GZ)
add('praRiso', 'R', '🟡', 'Riso al curry con pollo e piselli', 20, [RI, PO, OL, PIS, ['Yogurt bianco magro', '50 g'], ['Curry e curcuma', 'q.b.']],
    ['Marina il pollo a bocconcini con yogurt e spezie.', 'Cuocilo in padella 8 minuti con i piselli.', 'Servi sul riso.'],
    'https://ricette.giallozafferano.it/Bocconcini-di-pollo-con-yogurt-e-curcuma.html', GZ)
add('praRiso', 'R', '🥢', 'Riso saltato con pollo alla soia', 20, [['Riso basmati (cotto e freddo)', '70 g crudo'], PO, OL, PIS, ['Salsa di soia', '15 ml'], ['Uovo', '1']],
    ['Cuoci il riso e lascialo raffreddare (anche la sera prima).', 'Salta pollo e piselli, poi l’uovo strapazzato.', 'Aggiungi riso e soia, 2 minuti a fuoco alto.'],
    'https://ricette.giallozafferano.it/Pollo-alla-salsa-di-soia.html', GZ)
add('praRiso', 'R', '🍄', 'Risotto funghi e pollo allo zafferano', 30, [['Riso Carnaroli', '70 g'], PO, OL, ['Funghi', '150 g'], ['Zafferano', '1 bustina'], ['Brodo vegetale', '400 ml']],
    ['Tosta il riso, poi cuocilo col brodo.', 'Aggiungi i funghi a metà e lo zafferano alla fine.', 'Pollo saltato a parte, unito al momento.'],
    'https://ricette.giallozafferano.it/Risotto-giallo-ai-finferli.html', GZ)
add('praRiso', 'R', '🍋', 'Riso, pollo al limone e piselli', 20, [RI, PO, OL, PIS, ZU, ['Limone', '½']],
    ['Infarina appena il pollo a fettine e cuocilo con limone e un goccio d’acqua.', 'Salta piselli e zucchine.', 'Riso bianco e tutto sopra.'],
    'https://ricette.giallozafferano.it/Pollo-al-limone.html', GZ)
add('praRiso', 'R', '🌰', 'Riso con pollo alle mandorle', 25, [RI, PO, OL, ['Mandorle', '10 g'], ['Zucchine e peperoni', '200 g'], ['Salsa di soia', '10 ml']],
    ['Tosta le mandorle a secco.', 'Salta pollo e verdure, sfuma con soia e un po’ d’acqua.', 'Mandorle sopra e riso a parte.'],
    'https://ricette.giallozafferano.it/Pollo-alle-mandorle.html', GZ)

# ---------- PRANZO BERTO SENZA CARBOIDRATI: UOVA ----------
UO, MOZ = ['Uova', '3 (150 g)'], ['Mozzarella light', '125 g']
add('praUova', 'R', '🥚', 'Frittata di zucchine al forno', 25, [UO, MOZ, OL, ['Zucchine', '250 g']],
    ['Affetta sottili le zucchine e saltale 3 minuti.', 'Sbatti le uova, aggiungi zucchine e mozzarella a dadini.', 'Forno a 180 °C per 15 minuti.'],
    'https://ricette.giallozafferano.it/Frittata-di-zucchine-al-forno.html', GZ)
add('praUova', 'R', '🍅', 'Uova al purgatorio con mozzarella', 15, [UO, MOZ, OL, ['Passata di pomodoro', '200 g'], ['Basilico', 'q.b.']],
    ['Cuoci la passata 5 minuti.', 'Apri le uova nel sugo, coperchio, 5-6 minuti.', 'Mozzarella a pezzi negli ultimi 2 minuti.'],
    'https://www.fattoincasadabenedetta.it/ricetta/uova-al-purgatorio/', BEN)
add('praUova', 'R', '🌶️', 'Shakshuka light', 20, [UO, ['Mozzarella light o feta', '100 g'], OL, ['Peperoni', '150 g'], ['Pomodori pelati', '200 g'], ['Cumino e paprika', 'q.b.']],
    ['Stufa i peperoni con le spezie.', 'Aggiungi i pelati e cuoci 8 minuti.', 'Uova nel sugo, coperchio finché l’albume è rappreso.'],
    'https://ricette.giallozafferano.it/Shakshuka.html', GZ)
add('praUova', 'R', '🥬', 'Rotolo di frittata spinaci e mozzarella', 25, [UO, MOZ, OL, ['Spinaci', '250 g']],
    ['Sbatti le uova e versale sulla teglia con carta forno: 10 minuti a 180 °C.', 'Farcisci con spinaci saltati e mozzarella.', 'Arrotola e passa 5 minuti in forno.'],
    'https://ricette.giallozafferano.it/Rotolo-di-frittata-al-forno.html', GZ, we=True)
add('praUova', 'R', '🧁', 'Frittatine di verdure al forno', 25, [UO, MOZ, OL, ['Verdure miste (zucchine, peperoni, spinaci)', '250 g']],
    ['Taglia le verdure piccolissime.', 'Mescola con uova e mozzarella e versa negli stampini da muffin.', '20 minuti a 180 °C.'],
    'https://www.fattoincasadabenedetta.it/ricetta/frittatine-di-verdure-al-forno/', BEN, 'Si portano anche al lavoro.')
add('praUova', 'R', '🌱', 'Frittata primavera con finocchi', 20, [UO, MOZ, OL, ['Finocchi', '250 g'], ['Erba cipollina', 'q.b.']],
    ['Affetta i finocchi sottili e stufali 8 minuti.', 'Versa le uova sbattute e cuoci col coperchio.', 'Mozzarella a fette sopra a fine cottura.'],
    'https://ricette.giallozafferano.it/Frittata-primavera.html', GZ)

# ---------- PRANZO LEGUMI (TUTTI E DUE) ----------
FA, LE, LEGC = ['Farro o orzo', 'R:60g F:15g'], ['Legumi secchi', 'R:30g F:40g'], ['Legumi secchi (o 3x in scatola)', 'R:30g F:40g']
PB, PAR, OLL, VG = ['Petto di pollo', 'R:80g F:0'], ['Parmigiano', 'R:10g F:0'], ['Olio EVO', 'R:5ml F:3ml'], ['Verdura', '200g+150g']
add('praL', 'RF', '🍲', 'Zuppa di lenticchie e farro', 40, [['Lenticchie secche', 'R:30g F:40g'], FA, PB, PAR, OLL, ['Carota, sedano, cipolla', '200g+150g']],
    ['Soffriggi il trito con l’olio e un goccio d’acqua.', 'Aggiungi lenticchie, farro e acqua: 30-35 minuti.', 'Per Berto: pollo a dadini saltato a parte.'],
    'https://www.fattoincasadabenedetta.it/ricetta/zuppa-di-lenticchie/', BEN)
add('praL', 'RF', '🟠', 'Zuppa di ceci e zucca', 40, [['Ceci secchi (o in scatola)', 'R:30g F:40g'], FA, PB, PAR, OLL, ['Zucca', '200g+150g'], ['Rosmarino', 'q.b.']],
    ['Cuoci zucca e ceci con il rosmarino fino a farli cremosi.', 'Frulla metà zuppa.', 'Aggiungi il farro cotto (e il pollo per Berto).'],
    'https://www.fattoincasadabenedetta.it/ricetta/zuppa-di-ceci-e-zucca/', BEN)
add('praL', 'RF', '🍛', 'Zuppa di lenticchie al curry', 35, [['Lenticchie rosse', 'R:30g F:40g'], ['Riso basmati', 'R:60g F:15g'], PB, OLL, ['Carote e spinaci', '200g+150g'], ['Curry', 'q.b.']],
    ['Le lenticchie rosse non vanno ammollate: cuocile 20 minuti con carote e curry.', 'Spinaci negli ultimi 3 minuti.', 'Servi col riso.'],
    'https://www.fattoincasadabenedetta.it/ricetta/zuppa-di-lenticchie-al-curry/', BEN)
add('praL', 'RF', '🫘', 'Zuppa del contadino', 45, [['Fagioli e lenticchie secchi', 'R:30g F:40g'], FA, PB, PAR, OLL, ['Verza, carote, patata piccola', '200g+150g']],
    ['Cuoci legumi e verdure a pezzi in acqua 35 minuti.', 'Aggiungi il farro negli ultimi 20.', 'Olio a crudo.'],
    'https://ricette.giallozafferano.it/Zuppa-del-contadino.html', GZ)
add('praL', 'RF', '🍝', 'Pasta e lenticchie', 30, [['Lenticchie secche', 'R:30g F:40g'], ['Pasta corta integrale', 'R:60g F:15g'], PB, PAR, OLL, ['Carota, sedano, pomodoro', '200g+150g']],
    ['Cuoci le lenticchie col soffritto e un po’ di pomodoro.', 'Butta la pasta direttamente nella minestra.', 'Parmigiano e olio a crudo.'],
    'https://ricette.giallozafferano.it/Pasta-e-lenticchie.html', GZ)
add('praL', 'RF', '🍝', 'Pasta al ragù di ceci', 30, [['Ceci in scatola', 'R:90g F:120g'], ['Pasta integrale', 'R:60g F:15g'], PB, OLL, ['Passata e verdure tritate', '200g+150g']],
    ['Trita grossolanamente i ceci e cuocili con verdure e passata 15 minuti.', 'Condisci la pasta.', 'Per Berto: pollo a dadini nel sugo.'],
    'https://ricette.giallozafferano.it/Pasta-al-ragu-di-ceci.html', GZ)
add('praL', 'RF', '🌰', 'Zuppa ceci e castagne', 45, [['Ceci secchi', 'R:30g F:40g'], ['Castagne lessate', 'R:60g F:20g'], PB, OLL, ['Porro e carote', '200g+150g'], ['Rosmarino', 'q.b.']],
    ['Stufa il porro, aggiungi ceci e acqua: 30 minuti.', 'Castagne sbriciolate negli ultimi 10.', 'Olio e rosmarino a crudo.'],
    'https://www.fattoincasadabenedetta.it/ricetta/zuppa-ceci-e-castagne/', BEN, 'Le castagne prendono il posto del farro.', we=True)
add('praL', 'RF', '🥣', 'Zuppa di legumi e farro', 45, [['Mix di legumi secchi', 'R:30g F:40g'], FA, PB, PAR, OLL, ['Verdure per minestrone', '200g+150g']],
    ['Ammolla i legumi la sera prima.', 'Cuocili 40 minuti con le verdure, il farro negli ultimi 25.', 'Pollo saltato a parte per Berto.'],
    'https://blog.giallozafferano.it/pasticciedelixie/ricetta-zuppa-legumi-e-farro/', GZB)

# ---------- SABATO: RAGÙ MAGRO (BERTO, carne rossa) ----------
add('praRagu', 'R', '🍝', 'Pasta al ragù magro classico', 40, [['Pasta integrale', '100 g'], ['Macinato di manzo magro (5%)', '120 g'], ['Passata di pomodoro', '150 g'], ['Carota, sedano, cipolla', '100 g'], ['Parmigiano', '15 g'], OL],
    ['Soffriggi il trito con l’olio e un goccio d’acqua.', 'Rosola la carne, poi passata: almeno 30 minuti a fuoco basso.', 'Condisci la pasta e il parmigiano.'],
    'https://ricette.giallozafferano.it/Ragu-alla-bolognese.html', GZ, 'Contorno di finocchi crudi 200 g.', we=True)
add('praRagu', 'R', '🧆', 'Pasta con le polpettine al sugo', 40, [['Pasta integrale', '100 g'], ['Macinato di manzo magro (5%)', '120 g'], ['Pangrattato', '5 g'], ['Passata di pomodoro', '200 g'], ['Parmigiano', '15 g'], OL],
    ['Impasta carne, pangrattato e metà parmigiano: polpettine piccole.', 'Cuocile 15 minuti direttamente nella passata.', 'Condisci la pasta.'],
    'https://ricette.giallozafferano.it/Spaghetti-con-le-polpettine.html', GZ, we=True)
add('praRagu', 'R', '🌶️', 'Chili con carne e riso', 40, [['Riso basmati', '80 g'], ['Macinato di manzo magro (5%)', '120 g'], ['Fagioli rossi in scatola', '80 g'], ['Pomodori pelati', '150 g'], ['Peperone', '100 g'], OL],
    ['Rosola cipolla, peperone e carne.', 'Aggiungi pelati, fagioli e spezie: 25 minuti.', 'Servi col riso.'],
    'https://ricette.giallozafferano.it/Chili-con-carne.html', GZ, we=True)
add('praRagu', 'R', '🍔', 'Burger fatto in casa con patate al forno', 35, [['Macinato di manzo magro (5%)', '150 g'], ['Pane da burger integrale', '1 (70 g)'], ['Patate', '150 g'], ['Insalata e pomodoro', '150 g'], OL],
    ['Patate a spicchi al forno 30 minuti a 200 °C con l’olio.', 'Forma il burger e cuocilo in piastra 3-4 minuti per lato.', 'Componi con insalata e pomodoro.'],
    'https://ricette.giallozafferano.it/Hamburger-di-carne-fatti-in-casa.html', GZ, 'Il pranzo “sfizioso” del sabato.', we=True)

# ---------- PRANZO PESCA: PASTA ----------
PF, OF, PAF = ['Pasta integrale', '60 g'], ['Olio EVO', '5 ml'], ['Parmigiano', '20 g']
add('praFPasta', 'F', '🍅', 'Pasta zucchine e pomodorini', 20, [PF, OF, PAF, ['Zucchine e pomodorini', '150 g'], ['Basilico', 'q.b.']],
    ['Salta le zucchine a rondelle 5 minuti.', 'Aggiungi i pomodorini per 2 minuti.', 'Manteca la pasta col parmigiano.'],
    'https://www.fattoincasadabenedetta.it/ricetta/pasta-zucchine-e-pomodorini/', BEN)
add('praFPasta', 'F', '🥬', 'Pasta ricotta e spinaci', 15, [PF, OF, ['Ricotta light', '40 g'], ['Spinaci', '150 g']],
    ['Cuoci gli spinaci 3 minuti e frullali con la ricotta.', 'Allunga con acqua di cottura e condisci la pasta.'],
    'https://www.fattoincasadabenedetta.it/ricetta/pasta-ricotta-e-spinaci/', BEN)
add('praFPasta', 'F', '🎃', 'Pasta con la zucca', 25, [PF, OF, PAF, ['Zucca', '150 g'], ['Rosmarino', 'q.b.']],
    ['Cuoci la zucca a dadini con acqua finché si sfalda.', 'Condisci la pasta e manteca col parmigiano.'],
    'https://ricette.giallozafferano.it/Pasta-con-la-zucca.html', GZ)
add('praFPasta', 'F', '🍄', 'Pasta zucca e funghi', 25, [PF, OF, PAF, ['Zucca e funghi', '150 g']],
    ['Salta funghi e zucca con aglio e un mestolo d’acqua.', 'Manteca la pasta.'],
    'https://ricette.giallozafferano.it/Pasta-zucca-e-funghi.html', GZ)
add('praFPasta', 'F', '🥦', 'Pasta con broccoli', 20, [PF, OF, PAF, ['Broccoli', '150 g'], ['Peperoncino', 'q.b.']],
    ['Cuoci i broccoli nell’acqua della pasta.', 'Salta tutto con aglio e peperoncino, schiacciando qualche cima.'],
    'https://ricette.giallozafferano.it/Pasta-con-broccoli.html', GZ)
add('praFPasta', 'F', '🫛', 'Pasta piselli e ricotta', 15, [PF, OF, ['Ricotta light', '40 g'], ['Piselli', '150 g'], ['Menta', 'q.b.']],
    ['Cuoci i piselli 5 minuti con un goccio d’acqua.', 'Frullane metà con la ricotta e condisci la pasta.'],
    'https://ricette.giallozafferano.it/Tagliatelle-piselli-e-ricotta.html', GZ)
add('praFPasta', 'F', '🌿', 'Minestrone con pasta e pesto', 35, [['Pasta corta', '50 g'], OF, ['Pesto', '10 g'], ['Verdure per minestrone', '250 g']],
    ['Cuoci le verdure a dadini 20 minuti.', 'Butta la pasta nella minestra.', 'Pesto a crudo.'],
    'https://ricette.giallozafferano.it/Minestrone-di-pasta-verdura-e-pesto.html', GZ)
add('praFPasta', 'F', '🥕', 'Pasta all’ortolana', 20, [PF, OF, PAF, ['Peperoni, zucchine, melanzane', '150 g']],
    ['Taglia le verdure a dadini piccoli e saltale 8 minuti.', 'Condisci la pasta.'],
    'https://www.fattoincasadabenedetta.it/ricetta/pasta-all-ortolana/', BEN)

# ---------- PRANZO PESCA: RISO ----------
RF_, OR, PR = ['Riso', '60 g'], ['Olio EVO', '6 ml'], ['Parmigiano', '25 g']
add('praFRiso', 'F', '🎃', 'Risotto zucca e funghi', 30, [['Riso Carnaroli', '60 g'], OR, PR, ['Zucca e funghi', '150 g'], ['Brodo vegetale', '350 ml']],
    ['Cuoci zucca e funghi col riso, un mestolo di brodo alla volta.', 'Manteca col parmigiano, senza burro.'],
    'https://ricette.giallozafferano.it/Risotto-zucca-e-funghi.html', GZ)
add('praFRiso', 'F', '🥬', 'Risotto al radicchio', 25, [['Riso Carnaroli', '60 g'], OR, PR, ['Radicchio', '150 g'], ['Brodo vegetale', '350 ml']],
    ['Appassisci il radicchio, tosta il riso e cuoci col brodo.', 'Parmigiano alla fine.'],
    'https://ricette.giallozafferano.it/Risotto-radicchio-noci-e-Sbrinz-DOP.html', GZ, 'Versione senza noci e Sbrinz, con parmigiano.')
add('praFRiso', 'F', '🍂', 'Risotto autunnale', 30, [['Riso Carnaroli', '60 g'], OR, PR, ['Zucca, funghi, porro', '150 g'], ['Brodo vegetale', '350 ml']],
    ['Stufa le verdure, aggiungi il riso e il brodo poco alla volta.', 'Manteca col parmigiano.'],
    'https://ricette.giallozafferano.it/Risotto-autunnale.html', GZ)
add('praFRiso', 'F', '🫛', 'Riso piselli e zucchine al limone', 20, [RF_, OR, PR, ['Piselli e zucchine', '150 g'], ['Limone', '½']],
    ['Lessa il riso.', 'Salta piselli e zucchine, scorza di limone alla fine.', 'Unisci e manteca col parmigiano.'],
    'https://ricette.giallozafferano.it/Pasta-e-zucchine.html', GZ)
add('praFRiso', 'F', '🟡', 'Risotto allo zafferano e zucchine', 25, [['Riso Carnaroli', '60 g'], OR, PR, ['Zucchine', '150 g'], ['Zafferano', '1 bustina'], ['Brodo vegetale', '350 ml']],
    ['Cuoci il riso col brodo e le zucchine a dadini.', 'Zafferano e parmigiano alla fine.'],
    'https://ricette.giallozafferano.it/Risotto-giallo-ai-finferli.html', GZ)

# ---------- CENA: POLLO E TACCHINO (TUTTI E DUE) ----------
PP, OP, VV = ['Petto di pollo o tacchino', 'R:190g F:140g'], ['Olio EVO', 'R:12ml F:13ml'], ['Verdura di contorno', '200g+150g']
add('cenPol', 'RF', '🍋', 'Scaloppine di pollo al limone', 15, [PP, OP, ['Limone', '1'], ['Farina', '1 cucchiaio'], VV],
    ['Batti le fettine e infarinale appena.', 'Rosola 2 minuti per lato, sfuma con limone e mezzo bicchiere d’acqua.', 'Cuoci finché si forma la salsina.'],
    'https://ricette.giallozafferano.it/Scaloppine-di-pollo-al-limone.html', GZ)
add('cenPol', 'RF', '🍕', 'Petto di pollo alla pizzaiola', 20, [PP, OP, ['Passata o pelati', '150g+100g'], ['Origano e capperi', 'q.b.'], VV],
    ['Rosola le fettine 2 minuti per lato.', 'Aggiungi pomodoro, origano e capperi: 10 minuti col coperchio.'],
    'https://www.fattoincasadabenedetta.it/ricetta/petto-di-pollo-alla-pizzaiola/', BEN)
add('cenPol', 'RF', '🍊', 'Petto di pollo all’arancia', 20, [PP, OP, ['Arancia (succo e scorza)', '1'], VV],
    ['Rosola il pollo a fettine.', 'Sfuma col succo d’arancia e lascia restringere.', 'Scorza grattugiata alla fine.'],
    'https://www.fattoincasadabenedetta.it/ricetta/petto-di-pollo-allarancia/', BEN)
add('cenPol', 'RF', '🟡', 'Bocconcini di pollo yogurt e curcuma', 20, [PP, ['Olio EVO', 'R:8ml F:8ml'], ['Yogurt bianco magro', '60g+50g'], ['Curcuma e paprika', 'q.b.'], VV],
    ['Marina i bocconcini con yogurt e spezie anche solo 10 minuti.', 'Cuocili in padella 8-10 minuti finché la salsa si addensa.'],
    'https://ricette.giallozafferano.it/Bocconcini-di-pollo-con-yogurt-e-curcuma.html', GZ)
add('cenPol', 'RF', '🌰', 'Pollo alle mandorle', 25, [PP, ['Olio EVO', 'R:8ml F:8ml'], ['Mandorle', '10g+8g'], ['Salsa di soia', '15 ml'], ['Zucchine e cipolla', '200g+150g']],
    ['Tosta le mandorle a secco.', 'Salta pollo e verdure a fuoco alto, sfuma con soia e acqua.', 'Mandorle alla fine.'],
    'https://ricette.giallozafferano.it/Pollo-alle-mandorle.html', GZ)
add('cenPol', 'RF', '🫒', 'Petto di pollo alla puttanesca', 20, [PP, OP, ['Pomodorini', '150g+100g'], ['Olive e capperi', '20g+15g'], VV],
    ['Rosola il pollo a bocconcini.', 'Aggiungi pomodorini, olive e capperi: 10 minuti.'],
    'https://blog.giallozafferano.it/pelledipollo/ricetta-petto-di-pollo-alla-puttanesca/', GZB)
add('cenPol', 'RF', '🍄', 'Pollo con funghi', 25, [PP, OP, ['Funghi', '200g+150g'], ['Aglio e prezzemolo', 'q.b.']],
    ['Trifola i funghi con aglio.', 'Aggiungi il pollo a straccetti, 8 minuti.', 'Prezzemolo fresco.'],
    'https://www.fattoincasadabenedetta.it/ricetta/petto-di-pollo-con-funghi/', BEN, 'I funghi fanno da contorno.')
add('cenPol', 'RF', '🧅', 'Petto di pollo cipolle e marsala', 25, [PP, OP, ['Cipolle rosse', '150g+100g'], ['Marsala', 'un goccio'], VV],
    ['Stufa le cipolle affettate 10 minuti.', 'Aggiungi il pollo, sfuma col marsala e cuoci 8 minuti.'],
    'https://www.fattoincasadabenedetta.it/ricetta/petto-di-pollo-cipolle-e-marsala/', BEN)
add('cenPol', 'RF', '🌿', 'Involtini di tacchino alla salvia', 25, [['Fesa di tacchino a fettine', 'R:190g F:140g'], OP, ['Prosciutto crudo sgrassato', '20g+15g'], ['Salvia', 'q.b.'], VV],
    ['Su ogni fettina metti prosciutto e salvia, arrotola e chiudi.', 'Rosola e sfuma con vino bianco o acqua: 12 minuti.'],
    'https://blog.giallozafferano.it/specialit/involtini-di-fesa-di-tacchino-alla-salvia/', GZB)
add('cenPol', 'RF', '🍎', 'Petto di pollo alle mele', 20, [PP, OP, ['Mela', '100g+80g'], ['Timo', 'q.b.'], VV],
    ['Rosola il pollo a fettine.', 'Aggiungi la mela a spicchi sottili e un goccio d’acqua: 8 minuti.'],
    'https://blog.giallozafferano.it/pelledipollo/ricetta-petto-di-pollo-alle-mele-in-padella/', GZB)
add('cenPol', 'RF', '🥛', 'Petti di pollo al latte', 25, [PP, ['Olio EVO', 'R:8ml F:8ml'], ['Latte scremato', '150 ml'], ['Rosmarino', 'q.b.'], VV],
    ['Rosola il pollo.', 'Copri col latte e il rosmarino e cuoci piano 15 minuti finché il fondo è cremoso.'],
    'https://ricette.giallozafferano.it/Petti-di-pollo-al-latte.html', GZ)
add('cenPol', 'RF', '🥫', 'Padellata di pollo e verdure', 20, [PP, OP, ['Peperoni, zucchine, carote', '250g+200g']],
    ['Taglia tutto a listarelle.', 'Salta prima le verdure poi il pollo, a fuoco alto.'],
    'https://blog.giallozafferano.it/pelledipollo/ricetta-padellata-di-pollo-e-verdure/', GZB)

# ---------- CENA: POLPETTE (TUTTI E DUE) ----------
MC, PG, PS, OPP = ['Macinato di pollo o tacchino', 'R:180g F:130g'], ['Parmigiano e pangrattato', 'R:20g F:16g'], ['Passata di pomodoro', 'R:150g F:120g'], ['Olio EVO', 'R:5ml F:4ml']
add('cenPolp', 'RF', '🧆', 'Polpette di pollo al forno', 30, [MC, PG, ['Uovo', '1 per tutto l’impasto'], OPP, VV],
    ['Impasta tutto e forma le polpette.', 'Forno a 200 °C per 18-20 minuti, girandole a metà.'],
    'https://www.fattoincasadabenedetta.it/ricetta/polpette-pollo-al-forno/', BEN)
add('cenPolp', 'RF', '🍋', 'Polpette di tacchino al limone', 25, [MC, PG, ['Limone (scorza e succo)', '1'], OPP, VV],
    ['Scorza di limone nell’impasto.', 'Rosola le polpette e sfuma col succo e mezzo bicchiere d’acqua.'],
    'https://ricette.giallozafferano.it/Polpette-di-tacchino-al-limone.html', GZ)
add('cenPolp', 'RF', '🍅', 'Polpette al sugo', 35, [['Macinato di pollo, tacchino o manzo magro', 'R:180g F:130g'], PG, PS, OPP, VV],
    ['Forma le polpette.', 'Cuocile 20 minuti direttamente nella passata con basilico.'],
    'https://www.fattoincasadabenedetta.it/ricetta/polpette-al-sugo/', BEN, 'Col manzo vale come carne rossa della settimana.')
add('cenPolp', 'RF', '🍊', 'Polpette di pollo all’arancia', 25, [MC, PG, ['Arancia', '1'], OPP, VV],
    ['Impasta col succo di mezza arancia.', 'Cuoci in padella e sfuma col resto del succo.'],
    'https://ricette.giallozafferano.it/Polpette-di-pollo-all-arancia.html', GZ)
add('cenPolp', 'RF', '🟡', 'Polpette di tacchino al curry', 30, [MC, PG, ['Latte di cocco light', '80ml+60ml'], ['Curry', 'q.b.'], VV],
    ['Rosola le polpette.', 'Aggiungi latte di cocco e curry: 10 minuti finché la salsa si addensa.'],
    'https://ricette.giallozafferano.it/Polpette-di-tacchino-al-latte-di-cocco-e-curry.html', GZ, 'Togli 3 ml di olio: il cocco ha già grassi.')
add('cenPolp', 'RF', '🥒', 'Spiedini di polpette pollo e zucchine', 30, [MC, PG, ['Zucchine', '200g+150g'], OPP],
    ['Grattugia metà zucchina nell’impasto.', 'Infila polpette e rondelle di zucchina negli stecchi.', 'Forno 200 °C, 20 minuti.'],
    'https://www.fattoincasadabenedetta.it/ricetta/polpette-su-stecco-pollo-e-zucchine/', BEN)

# ---------- CENA: CARNE ROSSA (1-2 volte a settimana) ----------
MZ, OM = ['Manzo (tagliata, fettine o bistecca)', 'R:180g F:130g'], ['Olio EVO', 'R:10ml F:8ml']
add('cenCar', 'RF', '🥩', 'Tagliata rucola e pomodorini', 15, [MZ, OM, ['Rucola e pomodorini', '200g+150g'], ['Grana a scaglie', '10g+8g']],
    ['Piastra rovente: 2-3 minuti per lato.', 'Riposo 3 minuti, poi a fette.', 'Su rucola e pomodorini, olio a crudo.'],
    'https://ricette.giallozafferano.it/Tagliata-di-manzo-con-rucola-e-pomodorini.html', GZ)
add('cenCar', 'RF', '🍷', 'Tagliata al balsamico', 15, [MZ, OM, ['Aceto balsamico', '2 cucchiai'], VV],
    ['Cuoci la carne in piastra.', 'Riduci il balsamico 1 minuto in padella.', 'Glassa la tagliata a fette.'],
    'https://ricette.giallozafferano.it/Tagliata-al-balsamico.html', GZ)
add('cenCar', 'RF', '🍕', 'Fettine alla pizzaiola', 20, [['Fettine di manzo', 'R:180g F:130g'], OM, ['Pelati', '150g+100g'], ['Origano', 'q.b.'], VV],
    ['Scotta le fettine 1 minuto per lato.', 'Aggiungi pelati e origano: 10 minuti col coperchio.'],
    'https://ricette.giallozafferano.it/Carne-alla-pizzaiola.html', GZ)
add('cenCar', 'RF', '🫑', 'Straccetti di manzo e peperoni', 20, [MZ, OM, ['Peperoni', '200g+150g'], ['Salsa di soia', '10 ml']],
    ['Salta i peperoni a listarelle 8 minuti.', 'Aggiungi gli straccetti a fuoco alto 2 minuti.', 'Un goccio di soia.'],
    'https://www.fattoincasadabenedetta.it/ricetta/straccetti-di-manzo/', BEN)
add('cenCar', 'RF', '🫛', 'Spezzatino light con piselli', 70, [['Manzo per spezzatino', 'R:180g F:130g'], OM, ['Piselli', '150g+100g'], ['Passata', '100 g'], ['Carota e cipolla', '100 g']],
    ['Rosola la carne a pezzi con il soffritto.', 'Passata e acqua, cottura lenta 50 minuti.', 'Piselli negli ultimi 15.'],
    'https://blog.giallozafferano.it/ricettesuperlightdigiovi/spezzatino-light-manzo-piselli-con-il-bimby-e-senza/', GZB, we=True)
add('cenCar', 'RF', '🟨', 'Bistecca glassata alla senape', 15, [MZ, OM, ['Senape', '1 cucchiaino'], ['Miele', '3 g'], VV],
    ['Spennella la carne con senape e miele.', 'Piastra 2-3 minuti per lato.'],
    'https://ricette.giallozafferano.it/Bistecca-glassata-con-senape.html', GZ)
add('cenCar', 'RF', '🍜', 'Manzo all’olio (lesso)', 90, [['Manzo da lesso magro', 'R:180g F:130g'], OM, ['Carote e sedano', '200g+150g'], ['Limone', '½']],
    ['Cuoci la carne con le verdure in acqua per 1 ora e mezza.', 'Fai a fette, condisci con olio e limone.'],
    'https://www.fattoincasadabenedetta.it/ricetta/manzo-all-olio/', BEN, 'Il brodo serve per un risotto o un passato.', we=True)

# ---------- CENA: TOFU (BERTO) ----------
TF, OT, VT = ['Tofu naturale', '250 g'], ['Olio EVO', '5 ml'], ['Zucchine e piselli', '200 g']
add('cenTofu', 'R', '🥢', 'Tofu marinato in padella', 20, [TF, OT, ['Salsa di soia', '15 ml'], ['Zenzero e aglio', 'q.b.'], VT],
    ['Taglia il tofu a cubi e marinalo 10 minuti con soia, zenzero e aglio.', 'Rosolalo in padella finché è dorato.', 'Salta le verdure nella stessa padella.'],
    'https://www.fattoincasadabenedetta.it/ricetta/tofu-marinato/', BEN)
add('cenTofu', 'R', '🔥', 'Tofu croccante in padella', 20, [TF, OT, ['Amido di mais', '1 cucchiaio'], ['Paprika', 'q.b.'], VT],
    ['Asciuga bene il tofu, taglialo a cubi e passalo nell’amido con la paprika.', 'Cuoci in padella antiaderente girandolo spesso.'],
    'https://ricette.giallozafferano.it/Tofu-in-padella.html', GZ)
add('cenTofu', 'R', '🍄', 'Tofu con funghi e verdure saltati', 20, [TF, OT, ['Funghi e zucchine', '250 g'], ['Salsa di soia', '15 ml']],
    ['Rosola il tofu a cubi e mettilo da parte.', 'Salta funghi e zucchine, poi rimetti il tofu con la soia.'],
    'https://blog.giallozafferano.it/danicucina/tofu-con-funghi-e-verdure-saltati/', GZB)
add('cenTofu', 'R', '🟡', 'Tofu al curry', 25, [TF, OT, ['Latte di cocco light', '60 ml'], ['Curry', 'q.b.'], ['Piselli e carote', '200 g']],
    ['Rosola il tofu.', 'Aggiungi verdure, curry e latte di cocco: 10 minuti.'],
    'https://blog.giallozafferano.it/unacamerieraincucina2701/spezzatino-di-tofu-al-curry-con-riso/', GZB)
add('cenTofu', 'R', '🌶️', 'Mapo tofu light', 25, [TF, OT, ['Macinato di pollo', '50 g'], ['Salsa di soia', '15 ml'], ['Peperoncino e zenzero', 'q.b.'], ['Zucchine', '150 g']],
    ['Rosola il macinato con zenzero e peperoncino.', 'Aggiungi il tofu a cubi, soia e mezzo bicchiere d’acqua: 8 minuti.'],
    'https://www.fattoincasadabenedetta.it/ricetta/mapo-tofu/', BEN, 'Versione col pollo al posto del maiale.')
add('cenTofu', 'R', '🫘', 'Fagiolini e tofu in padella', 20, [TF, OT, ['Fagiolini', '200 g'], ['Salsa di soia', '15 ml'], ['Sesamo', '5 g']],
    ['Sbollenta i fagiolini 5 minuti.', 'Salta con il tofu e la soia, sesamo alla fine.'],
    'https://blog.giallozafferano.it/lericettediberry/fagiolini-e-tofu-in-padella/', GZB)

# ---------- CENA BERTO: FRITTATA / UOVA ----------
U2, AL, PU, OU = ['Uova', '2 (100 g)'], ['Albumi', '200 g'], ['Parmigiano', '15 g'], ['Olio EVO', '5 ml']
add('cenUova', 'R', '🥬', 'Frittata di albumi e spinaci', 15, [U2, AL, PU, OU, ['Spinaci', '200 g']],
    ['Salta gli spinaci.', 'Sbatti uova, albumi e parmigiano e versa sopra.', 'Coperchio, fuoco basso, 6-8 minuti.'],
    'https://ricette.giallozafferano.it/Frittata-primavera.html', GZ)
add('cenUova', 'R', '🥒', 'Frittata di zucchine al forno', 25, [U2, AL, PU, OU, ['Zucchine', '200 g']],
    ['Zucchine a rondelle sottili.', 'Mescola con uova e albumi, teglia con carta forno: 180 °C per 18 minuti.'],
    'https://ricette.giallozafferano.it/Frittata-di-zucchine-al-forno.html', GZ)
add('cenUova', 'R', '🌯', 'Rotolini di frittata con verdure', 20, [U2, AL, PU, OU, ['Zucchine grigliate e insalata', '200 g']],
    ['Fai 2-3 frittatine sottili.', 'Farcisci con le verdure e arrotola.'],
    'https://www.fattoincasadabenedetta.it/ricetta/rotolini-di-frittata/', BEN)
add('cenUova', 'R', '🍅', 'Shakshuka con albumi', 20, [U2, AL, PU, OU, ['Peperoni e pelati', '250 g']],
    ['Cuoci peperoni e pelati 10 minuti.', 'Versa gli albumi, poi le uova intere: coperchio 6 minuti.'],
    'https://www.fattoincasadabenedetta.it/ricetta/shakshuka/', BEN)
add('cenUova', 'R', '🧁', 'Muffin di frittata alle verdure', 25, [U2, AL, PU, OU, ['Verdure miste a dadini', '200 g']],
    ['Mescola tutto e versa negli stampini.', 'Forno 180 °C per 20 minuti.'],
    'https://www.fattoincasadabenedetta.it/ricetta/frittatine-di-verdure-al-forno/', BEN)

# ---------- CENA PESCA: PESCE ----------
SA, VF = ['Salmone', '160 g'], ['Verdura', '150 g']
add('cenSal', 'F', '🍋', 'Salmone in padella', 15, [SA, VF, ['Limone', '½']],
    ['Padella calda senza olio: salmone dal lato della pelle 5 minuti.', 'Giralo 2 minuti, limone alla fine.'],
    'https://www.fattoincasadabenedetta.it/ricetta/salmone-in-padella/', BEN, 'Il salmone ha già i suoi grassi: niente olio.')
add('cenSal', 'F', '🔥', 'Salmone al forno', 20, [SA, VF, ['Erbe aromatiche', 'q.b.']],
    ['Forno a 200 °C per 12-15 minuti con le erbe.', 'Verdure in teglia accanto.'],
    'https://ricette.giallozafferano.it/Salmone-al-forno.html', GZ)
add('cenSal', 'F', '♨️', 'Salmone al vapore', 15, [SA, VF, ['Salsa di soia', '5 ml']],
    ['Cuoci a vapore 8-10 minuti insieme alle verdure.', 'Un goccio di soia.'],
    'https://www.fattoincasadabenedetta.it/ricetta/salmone-al-vapore/', BEN)
add('cenSal', 'F', '🍅', 'Salmone con pomodorini e olive', 20, [SA, ['Pomodorini', '150 g'], ['Olive', '10 g']],
    ['Salta pomodorini e olive 3 minuti.', 'Adagia il salmone, coperchio 8 minuti.'],
    'https://blog.giallozafferano.it/ilcaldosaporedelsud/ricetta-salmone-con-pomodorini-cipolla-e-olive/', GZB)
add('cenSal', 'F', '🍋', 'Scaloppine di salmone al limone', 15, [SA, VF, ['Limone', '½'], ['Farina', '1 cucchiaino']],
    ['Taglia il salmone a fette di 1 cm e infarinale appena.', '1 minuto per lato e sfuma col limone.'],
    'https://www.fattoincasadabenedetta.it/ricetta/scaloppine-di-salmone/', BEN)
add('cenSal', 'F', '🐟', 'Filetti di merluzzo al forno', 20, [['Merluzzo o orata', '200 g'], ['Olio EVO', '8 ml'], VF, ['Pangrattato e prezzemolo', '10 g']],
    ['Pangrattato e prezzemolo sui filetti.', 'Forno 200 °C per 15 minuti.'],
    'https://ricette.giallozafferano.it/Filetti-di-merluzzo-al-forno.html', GZ, 'Per il venerdì.')
add('cenSal', 'F', '🍊', 'Merluzzo agli agrumi', 15, [['Merluzzo', '200 g'], ['Olio EVO', '8 ml'], VF, ['Arancia e limone', '½ + ½']],
    ['Cuoci il merluzzo in padella 4 minuti per lato.', 'Sfuma con il succo degli agrumi.'],
    'https://ricette.giallozafferano.it/Merluzzo-agli-agrumi.html', GZ, 'Per il venerdì.')
add('cenSal', 'F', '🧀', 'Merluzzo gratinato', 25, [['Merluzzo', '200 g'], ['Olio EVO', '8 ml'], VF, ['Pangrattato e parmigiano', '12 g']],
    ['Copri i filetti con pangrattato e parmigiano.', 'Forno 200 °C per 15 minuti, poi 2 minuti di grill.'],
    'https://www.fattoincasadabenedetta.it/ricetta/merluzzo-gratinato-al-forno/', BEN, 'Per il venerdì.')

# ---------- CENA PESCA: PASSATI E VELLUTATE ----------
PV = [['Uovo sodo', '1'], ['Parmigiano', '20 g'], ['Fette biscottate', '10 g']]
add('cenFPass', 'F', '🎃', 'Vellutata di zucca', 30, [['Zucca', '250 g'], ['Patata', '50 g'], ['Brodo vegetale', '200 ml']] + PV,
    ['Cuoci zucca e patata a pezzi nel brodo 20 minuti.', 'Frulla, parmigiano sopra; uovo sodo a parte.'],
    'https://www.fattoincasadabenedetta.it/ricetta/vellutata-zucca/', BEN)
add('cenFPass', 'F', '🥕', 'Vellutata di zucca e carote', 30, [['Zucca e carote', '300 g'], ['Brodo vegetale', '200 ml']] + PV,
    ['Cuoci le verdure nel brodo 20 minuti.', 'Frulla e servi con l’uovo sodo.'],
    'https://ricette.giallozafferano.it/Vellutata-di-zucca-e-carote.html', GZ)
add('cenFPass', 'F', '🥣', 'Passato di verdure', 35, [['Verdure miste', '300 g'], ['Brodo vegetale', '200 ml']] + PV,
    ['Cuoci tutte le verdure 25 minuti.', 'Passa col frullatore a immersione.'],
    'https://ricette.giallozafferano.it/Passato-di-verdure.html', GZ)
add('cenFPass', 'F', '🍄', 'Vellutata di zucca e funghi', 30, [['Zucca e funghi', '300 g'], ['Brodo vegetale', '200 ml']] + PV,
    ['Tieni da parte qualche fungo trifolato.', 'Cuoci e frulla il resto, funghi sopra.'],
    'https://www.fattoincasadabenedetta.it/ricetta/vellutata-di-zucca-e-funghi/', BEN)
add('cenFPass', 'F', '🥒', 'Vellutata zucca e zucchine', 25, [['Zucca e zucchine', '300 g'], ['Brodo vegetale', '200 ml']] + PV,
    ['Cuoci le verdure 15 minuti nel brodo.', 'Frulla e servi tiepida.'],
    'https://www.fattoincasadabenedetta.it/ricetta/vellutata-di-zucca-e-zucchine/', BEN)

if __name__ == '__main__':
    json.dump(R, open('ric.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    import collections
    print(len(R), dict(collections.Counter(r['slot'] for r in R)))
