# -*- coding: utf-8 -*-

import json
import re

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

  mingxinglist.append(mingxing)

mingxingfile_processed.write(json.dumps(mingxinglist, ensure_ascii=False, indent=2))
