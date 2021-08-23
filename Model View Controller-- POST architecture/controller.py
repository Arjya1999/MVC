# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:03:52 2021

@author: ARJYA
"""


from flask import Flask,render_template,url_for,request,redirect
from model import get_data

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    data=get_data()
    
    return redirect(url_for("display", data = data))

@app.route('/display/<data>',methods=['POST','GET'])
def display(data):
    
    return render_template('result.html', prediction = data)

if __name__ == '__main__':
	app.run(debug=True)
