import operator
import re
import json
from pyhanlp import *
import pydash

mingxinglist = json.loads(open('mingxing_processed.json', 'r').read())
guanxifile = open('guanxi1.txt', 'w')

guanxi = {}
guanxilist = []
guanxistr = ''

for mingxing in mingxinglist:
  relations = ''.join(mingxing['relations'].split('\n'))
  if not relations:
    continue

  fenci = HanLP.segment(relations)
  for ci in fenci:
    word = str(ci.word)
    nature = str(ci.nature)
    if len(word) == 1:
      continue
    if word in guanxi.keys():
      guanxi[word] = guanxi[word] + 1
    else:
      guanxi[word] = 1
      continue

for gx in guanxi:
  nature = HanLP.segment(gx)
  guanxilist.append({
    'name': gx,
    'count': guanxi[gx],
    'nature': str(nature[0].nature)
  })

guanxilist = pydash.collections.order_by(guanxilist, ['count'], reverse=True)

for gx in guanxilist:
  guanxistr = guanxistr + gx.get('name') + ' ' + str(gx.get('count')) + ' ' + str(gx.get('nature')) + '\n'

guanxifile.write(guanxistr)
guanxifile.close()
