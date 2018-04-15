import requests
import json


url = 'https://api.dongqiudi.com/data/v1/person/statistic_new/50432357'
page = json.loads(requests.get(url).text)
print page
if 'league' in page:
    print 'ds'
else:
    print 'sdfsd'
