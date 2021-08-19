# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:03:52 2021

@author: ARJYA
"""


from flask import Flask,render_template,url_for,request
import requests
import json

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    data=requests.request("POST",url="http://127.0.0.1:5000/data")
    
    with open(data, 'r') as j:
        data = json.loads(j.read())

    if request.method == 'POST':
        return data
    else:
        return data

if __name__ == '__main__':
	app.run(debug=True)
