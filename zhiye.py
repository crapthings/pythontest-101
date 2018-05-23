import json

personlist = json.loads(open('mingxing_processed.json', 'r').read())
zhiyefile = open('zhiye1.txt', 'w')

zhiyestr = ''

for person in personlist:
  for zhiye in person.get('labels').split('、'):
    if zhiye:
      zhiyestr += zhiye + '\n'

zhiyefile.write(zhiyestr)
