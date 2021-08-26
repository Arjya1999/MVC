# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:13:52 2021

@author: ARJYA
"""

from flask import Flask, jsonify
from flask_restx import Resource
import redis

r = redis.Redis(host='localhost',port=6379)

data={"name":"Arjya Basu","gender":"male","Age":"22"}

for i in data:
    r.set(i,data[i])

class HelloWorld(Resource):

    def get(self):
        return jsonify({"Hello": str(r.get("name"))[2:-1]})
    
    def post(self):
        return jsonify({"Hello": str(r.get("Age"))[2:-1]})

    def delete(self):
        return jsonify({"Hello": str(r.get("gender"))[2:-1]})

    def put(self):
        return jsonify({"Hello": "put"})