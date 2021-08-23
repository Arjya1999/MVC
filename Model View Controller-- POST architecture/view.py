# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:29:07 2021

@author: ARJYA
"""

import redis
import requests
import json

r = redis.Redis(host='localhost',port=6379)

data=requests.request("POST",url="http://127.0.0.1:5000/")

data=json.loads(data.content)

for i in data:
    r.set(i,data[i])

print(r.get("name"))
print(r.get("Age"))