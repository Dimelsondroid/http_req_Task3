import requests
import json
from pprint import pprint
import datetime

tag = 'Python'
url = 'https://api.stackexchange.com/2.3/questions'

now = datetime.datetime.now()
present_day = now.strftime('%d')
days_ago_2 = str(int(present_day) - 2)
from_date = now.strftime('%Y-%m-'+ days_ago_2)
to_date = now.strftime('%Y-%m-'+ present_day)

parameters = {
    'fromdate': from_date,
    'todate': to_date,
    'order': 'desc',
    'sort': 'activity',
    'tagged': tag,
    'filter': 'default',
    'site': 'stackoverflow'
}

req = requests.get(url, parameters)
for item in req.json()['items']:
    pprint(item['title'])
