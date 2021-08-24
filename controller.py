# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:13:52 2021

@author: ARJYA
"""

from flask import Flask
from flask_restx import Resource,Api
'''
app=Flask('__name__')
api=Api(app)

@api.route("/hello", methods=['GET'])
'''
class HelloWorld(Resource):
    def get(self):
        return {'hello':'get'}
    
    def post(self):
        return {'hello':'post'}

    def put(self):
        return {'hello':'put'}

    def delete(self):
        return {'hello':'delete'}
'''
if __name__ == '__main__':
    app.run(debug=True)
  '''  