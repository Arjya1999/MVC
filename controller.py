# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:13:52 2021

@author: ARJYA
"""

from flask import Flask, jsonify
from flask_restx import Resource

class HelloWorld(Resource):

    def get(self):
        return jsonify({"Hello":"get"})
    
    def post(self):
        return jsonify({"Hello": "post"})

    def delete(self):
        return jsonify({"Hello": "delete"})

    def put(self):
        return jsonify({"Hello":"put"})