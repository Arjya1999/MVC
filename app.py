# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:18:35 2021

@author: ARJYA
"""

from flask import Flask
from flask_restx import Api
from controller import *

app=Flask('__name__')

api=Api(app)

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
