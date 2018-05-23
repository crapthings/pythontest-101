# -*- coding: utf-8 -*-

import json
import re
from pyhanlp import *

mingxingfile = json.loads(open('mingxing_unprocessed.json').read())

mingxingfile_processed = open('mingxing_processed.json', 'w')

mingxinglist = []

for item in mingxingfile:
  mingxing = {}

  mingxing['name'] = item['name']

  mingxing['summary'] = re.sub('\\n\[.*?\].\\n', '\n', item['summary'])

  mingxing['works'] = re.sub('^\\n', '', item['works'])

  mingxing['relations'] = re.sub('^\\n', '', item['relations'])
  mingxing['relations'] = re.sub('$\\n', '', item['relations'])

  labels = ''
  for label in HanLP.segment(mingxing['summary']):
    word = str(label.word)
    # print(label.nature, label.word)
    if str(label.nature) in ['nnt', 'nnd'] and word not in labels:
      labels += word + '、'

  mingxing['labels'] = labels

  mingxinglist.append(mingxing)

mingxingfile_processed.write(json.dumps(mingxinglist, ensure_ascii=False, indent=2))
