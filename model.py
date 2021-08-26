# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:53:40 2021

@author: ARJYA
"""
import json
'''
import redis

r = redis.Redis(host='localhost',port=6379)
  '''
# Opening JSON file
f = open('sample.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

def display():
    
    return data

def display_by_id(id):
    
    return data[id]

def add(dataset):
    data[str(len(data)+1)]=dataset
    json_object = json.dumps(data)
  
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
        
    return data

def delete(ids):
    del data[ids]
    json_object = json.dumps(data)
  
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
        
    return "The information of row "+ids+" is deleted"

def update(ids,name,age,gender):
    d1={}
    if name!=None:
        d1.update({"name":name})
    if age!=None:
        d1.update({"Age":age})
    if gender!=None:
        d1.update({"gender":gender})
    data.update({ids:d1})
    json_object = json.dumps(data)
  
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
        
    return "The dictionary was updated"