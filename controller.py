from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *
from helper import *

var = DataHandling()

class RecordHandling(Resource):
    
    def get(self):
        try:
            ids = request.get_json()
            
            if ids== None:
                display_all_records = var.display()
                return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's get method", data=display_all_records, status_code=200)
            else:
                return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's get method", data=var.display_record_by_id(ids['ids']), status_code=200)

        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from RecordHandling's get method", data=None, status_code=400)

    def post(self):
        try:
            data_request_json = request.get_json()
            dataset = {}
            dataset.update({"name":data_request_json['name'],"Age":data_request_json['Age'],"gender":data_request_json['gender']})
            
            results = var.add(dataset)

            return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's post method", data = results, status_code=200)            
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from RecordHandling's post method", data=None, status_code=400)
        
    def delete(self):
        try:
            data_request_json =request.get_json()
            
            info = var.delete(data_request_json['ids'])
            
            return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's delete method", data = info['message'], status_code=200)
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from RecordHandling's delete method", data=None, status_code=400)

    def put(self):
        try:
            data_request_json = request.get_json()
        
            results = var.update(
                data_request_json['ids'], data_request_json['name'], data_request_json['Age'], data_request_json['gender'])

            return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's put method", data = results['message'], status_code=200)            
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from RecordHandling's put method", data=None, status_code=400)

class_object = HistogramHandling()

class Histogram(Resource):
    
    def get(self):
        try:
            column_name = request.get_json()
            
            data_histogram = class_object.histogram(column_name['column name'])
            return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data=data_histogram, status_code=200)

        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from Histogram's get method", data=None, status_code=400)
