#!/usr/bin/python
# coding: utf-8
import json
import os

lang_list = ["de","fr","ja","pt_br","ru","zh_cn","zh_hk"]
rf_en = open('PokemonGo-Map/static/locales/pokemon.en.json', 'r')
json_data_en = json.load(rf_en)
  
for lang in lang_list:
  print "Encode : %s" % lang
  rf = open('PokemonGo-Map/static/locales/pokemon.%s.json' % lang, 'r')
  if not os.path.exists("res/values-%s" % lang):
    os.makedirs("res/values-%s" % lang)
  wf = open('res/values-%s/pokemon.xml' % lang, 'w')
  json_data_l = json.load(rf)
  wf.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n");

  for n in range(1, len(json_data_l)):
    if str(n) in json_data_l:
      wf.write("\t<string name=\"{0}\">{1}</string>\n".format(json_data_en[str(n)].lower().replace(".","").replace(" ", "_").replace("'", "").replace("-", "").encode('utf-8').replace("♂","_male").replace("♀","_famale"), json_data_l[str(n)].encode('utf-8')));

  wf.write("</resources>");
  rf.close()
  wf.close()

#Defalut
if not os.path.exists("res/values"):
  os.makedirs("res/values")
wf = open('res/values/pokemon.xml', 'w')
wf.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n");

for n in range(1, len(json_data_en)):
  wf.write("\t<string name=\"{0}\">{1}</string>\n".format(json_data_en[str(n)].lower().replace(".","").replace(" ", "_").replace("'", "").replace("-", "").encode('utf-8').replace("♂","_male").replace("♀","_famale"), json_data_en[str(n)].encode('utf-8')));

wf.write("</resources>");

rf_en.close()
wf.close()

