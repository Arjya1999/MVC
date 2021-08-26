# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:13:52 2021

@author: ARJYA
"""

from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *

class HelloWorld(Resource):

    def get(self):
        ids = request.args.getlist('ids')
        print(ids)
        status=200
        if ids== []:
            try:
                return jsonify({"status":200,"message":"OK, Returning data from get method","Hello": display()})
            except:
                return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method"})
        else:
            try:
                return jsonify({"status":200,"message":"OK, Returning data from get method","Hello": display_by_id(ids[0])})
            except:
                return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method"})
    
    def post(self):
        name = request.args.getlist('name')
        Age = request.args.getlist('Age')
        gender = request.args.getlist('gender')
        try:
            return jsonify({"status":200,"message":"OK, Returning data from get method","Hello": add({"name":name[0],"Age":Age[0],"gender":gender[0]})})
        except:
            return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method"})
        
    def delete(self):
        ids= request.args.getlist('ids')
        return jsonify({"status":200,"message":"OK, Returning data from get method","Hello": delete(ids[0])})

    def put(self):
        ids= request.args.getlist('ids')
        return jsonify({"status":200,"message":"OK, Returning data from put method","Hello": update(ids[0],name[0],Age[0],gender[0])})