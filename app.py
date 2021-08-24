# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:18:35 2021

@author: ARJYA
"""

from flask import Flask
from flask_restx import Resource,Api
from controller import HelloWorld

app=Flask('__name__')

api=Api(app)

#api.route('/hello',methods=['GET'])(HelloWorld().get())
api.add_resource(HelloWorld(Resource).get(), '/get')
api.add_resource(HelloWorld(Resource).post(), '/post')

if __name__ == '__main__':
    app.run(debug=True)