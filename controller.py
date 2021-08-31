from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *

class RecordHandling(Resource):
    
    def __init__(self):
        self.var=DataHandling()
    
    def get(self):
        try:
            ids = request.get_json()
            
            if ids== None:
                display_all_records= self.var.display()
                return jsonify({"success":True,"message":"OK, Returning data from get method","data": display_all_records})
            else:
                display_record_by_id= self.var.display_by_id(ids['ids'])
                return jsonify({"success":True,"message":"OK, Returning data from get method","data": display_record_by_id})
        except:
            return jsonify({"success":False, "message":"Bad Request, Some error has occured while returning data from get method","data":[]})
    
    def post(self):
        try:
            data_request_json = request.get_json()
            dataset = {}
            dataset.update({"name":data_request_json['name'],"Age":data_request_json['Age'],"gender":data_request_json['gender']})
            
            results = self.var.add(dataset)
            
            return jsonify({"success":True,"message":"OK, Returning data from post method","data": results})
        except:
            return jsonify({"success":False, "message":"Bad Request, Some error has occured while returning data from post method","data":[]})
        
    def delete(self):
        try:
            data_request_json =request.get_json()
            
            info = self.var.delete(data_request_json['ids'])
            
            return jsonify({"success":True,"message":"OK, Returning data from delete method","data": info['message']})
        except:
            return jsonify({"success":False, "message":"Bad Request, Some error has occured while returning data from delete method","data":[]})

    def put(self):
        try:
            data_request_json = request.get_json()
        
            results = self.var.update(data_request_json['ids'], data_request_json['name'], data_request_json['Age'], data_request_json['gender'])
            
            return jsonify({"status":200,"message":"OK, Returning data from put method","data": results['message']})
        except:
            return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from put method","data":[]})