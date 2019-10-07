from __future__ import absolute_import
from Qshop.celery import app

@app.task
def task_example():
    return 'i am taskexample'


import json
import requests
from Qshop.settings import DingURL

@app.task
def sendDing(content='1111111',to=None):
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8'
    }
    requests_data = {
        'msgtype': 'text',
        'text': {
            'content': content
        },
        'at': {
            'atMobiles': [
            ],
            'isAtAll': True
        }
    }
    if to:
        requests_data['at']['atMobiles'].append(to)
        requests_data['at']['isAtAll']=False
    else:
        requests_data['at']['atMobiles'].clear()
        requests_data['at']['isAtAll']=True

    sendData = json.dumps(requests_data)
    response = requests.post(url=DingURL, headers=headers, data=sendData)
    content = response.json()
    return content
