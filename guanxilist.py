import operator
import re
import json
from pyhanlp import *
import pydash

mingxinglist = json.loads(open('mingxing_processed.json', 'r').read())

guanxi = {}
guanxilist = []

for mingxing in mingxinglist:
  relations = ''.join(mingxing['relations'].split('\n'))
  if not relations:
    continue

  fenci = HanLP.segment(relations)
  for ci in fenci:
    word = str(ci.word)
    nature = str(ci.nature)
    dir(guanxi)
    if len(word) == 1:
      continue
    if word in guanxi.keys():
      guanxi[word] = guanxi[word] + 1
    else:
      guanxi[word] = 1
      continue

for gx in guanxi:
  guanxilist.append({
    'name': gx,
    'count': guanxi[gx]
  })

guanxilist = pydash.collections.order_by(guanxilist, ['count'], reverse=True)

print(guanxilist)
