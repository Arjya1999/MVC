# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:40:40 2021

@author: ARJYA
"""
import json
import redis

def data(data):
  
# Data to be written
    dictionary ={
        "name" : data
    }
      
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 1)
      
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)