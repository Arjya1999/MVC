from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *
from helper import *

class RecordHandling(Resource,DataHandling):
    
    def __init__(self):
        super().__init__(self)
    
    def get(self):
        try:
            ids = request.get_json()
            
            if ids == None:
                display_all_records= self.display()
                return getCustomResponse(success=True, message="OK, Returning data from get method", data=display_all_records, status_code=200)
            else:
                return getCustomResponse(success=True, message="OK, Returning data from get method", data=display_record_by_id(ids['ids']), status_code=200)

        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from get method", data=None, status_code=400)
    
    def post(self):
        try:
            data_request_json = request.get_json()
            dataset = {}
            dataset.update({"name":data_request_json['name'],"Age":data_request_json['Age'],"gender":data_request_json['gender']})
            
            results = self.add(dataset)

            return getCustomResponse(success=True, message="OK, Returning data from post method", data = results, status_code=200)            
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from post method", data=None, status_code=400)
        
    def delete(self):
        try:
            data_request_json =request.get_json()
            
            info = self.delete(data_request_json['ids'])
            
            return getCustomResponse(success=True, message="OK, Returning data from delete method", data = info['message'], status_code=200)
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from delete method", data=None, status_code=400)

    def put(self):
        try:
            data_request_json = request.get_json()
        
            results = self.update(data_request_json['ids'], data_request_json['name'], data_request_json['Age'], data_request_json['gender'])

            return getCustomResponse(success=True, message="OK, Returning data from put method", data = results['message'], status_code=200)            
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from put method", data=None, status_code=400)
