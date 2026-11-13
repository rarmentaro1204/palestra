# Ricostruisce index.html da src/: python3 build.py
import json, subprocess, sys
subprocess.run([sys.executable, 'src/foods.py'], check=True)
a = open('src/app.html', encoding='utf-8').read()
d = json.dumps(json.load(open('src/data1.json', encoding='utf-8')), ensure_ascii=False, separators=(',', ':'))
r = json.dumps(json.load(open('src/ric.json', encoding='utf-8')), ensure_ascii=False, separators=(',', ':'))
f = open('src/foods.json', encoding='utf-8').read()
open('index.html', 'w', encoding='utf-8').write(a.replace('/*DATA*/', d).replace('/*RIC*/', r).replace('/*FOODS*/', f))
