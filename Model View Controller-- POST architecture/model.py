# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:31:31 2021

@author: ARJYA
"""
import json
import redis

r = redis.Redis(host='localhost',port=6379)

def get_data():

    f = open('data.json',)
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    for i in data:
        r.set(i,data[i])
    
    return(r.get("name"))
