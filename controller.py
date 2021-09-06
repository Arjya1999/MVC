from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *
from helper import *
from data_visualization import *

var = DataHandling()

# dynamic function calling
dynamic = {"display":var.display,"displaybyid":var.display_record_by_id}

class RecordHandling(Resource):

    def get(self):
        try:
            name="display"
            ids = request.get_json()
            
            if ids== None:
                func_name=dynamic[name]
                display_all_records = func_name()
                return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's get method", data=display_all_records, status_code=200)            
            else:
                name=name+"byid"
                func_name=dynamic[name]
                display_by_id = func_name(ids['ids'])
                return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's get method", data= display_by_id, status_code=200)
        
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

class_object = DataVisualization()

class Visualization(Resource):
    
    def get(self):
        try:
            data_from_json = request.get_json()
            graph_name= data_from_json["graph name"].lower()

            if graph_name == "histogram":
                data_histogram = class_object.histogram(data_from_json['column name'])
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data=data_histogram, status_code=200)
            elif graph_name == "line chart":
                column_name1 = data_from_json['column name 1']
                column_name2 = data_from_json['column name 2']
                data_linechart = class_object.linechart(column_name1,column_name2)
                
                return getCustomResponse(success=True, message="OK, Returning data from Visualization's get method", data=data_linechart, status_code=200)
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from Visualization's get method", data=None, status_code=400)
