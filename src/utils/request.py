import yaml
import sys
sys.path.append('../../')
import config
import requests
import json
# from crawler import *
# from generate_table import *

def request_API(API):
    global json_load
    response_API = requests.get(API)
    if response_API.status_code == 200:
        data = response_API.text
        json_load = json.loads(data)
    else:
        pass
    return json_load

def request_image(link, filename):

    payload={}
    headers = {
      'Cookie': '_cfuvid=Q1a0Cvoh6_5F4cbZcwlq_sdw93DFYHzAR5TsQSAtUtg-1667363759153-0-604800000'
    }

    res = requests.request("GET", link, headers=headers, data=payload)
    
    if res.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(res.content)
    return None