# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:40:40 2021

@author: ARJYA
"""
from flask import Flask,render_template,url_for,request
import json

# load the model from disk
json_file_path='New Text Document.json'
with open(json_file_path, 'r') as j:
     data = json.loads(j.read())
     
app = Flask(__name__)

@app.route('/data',methods=['POST','GET'])
def data():
    if request.method == 'POST':
        
        return data
    else:
        return data

if __name__ == '__main__':
	app.run(debug=True)
