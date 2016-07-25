#!/usr/bin/python
# coding: utf-8
import json

f = open('pokemon.ja.json', 'r')
fen = open('pokemon.en.json', 'r')

json_data_l = json.load(f)
json_data_en = json.load(fen)

print "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>"

for n in range(1, len(json_data_en)):
  print "\t<string name=\"{0}\">{1}</string>".format(json_data_en[str(n)].encode('utf-8'), json_data_l[str(n)].encode('utf-8'));

print "</resources>"

f.close()
