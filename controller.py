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
            try:
                column_name1 = data_from_json['column name 1']
            except:
                pass

            if graph_name == "histogram":
            
                data_histogram = class_object.histogram(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data=data_histogram, status_code=200)
            
            elif graph_name == "graph distribution":
            
                data_graph_distribution = class_object.graph_distribution(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_graph_distribution, status_code=200)
            
            elif graph_name == "skewness":
                
                data_skewness = class_object.skewness(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_skewness, status_code=200)
            
            elif graph_name == "boxplot":
                
                data_boxplot = class_object.boxplot(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_boxplot, status_code=200)
            
            elif graph_name == "graph for column relation with target variable":
            
                data_correlation_with_target_variable = class_object.graph_for_column_relation_with_target_variable(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_correlation_with_target_variable, status_code=200)
            
            elif graph_name == "bar graph":
            
                data_bar_graph = class_object.Bargraph(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_bar_graph, status_code=200)
                        
            elif graph_name == "line chart":
                
                column_name2 = data_from_json['column name 2']
                data_linechart = class_object.linechart(column_name1,column_name2)
                
                return getCustomResponse(success=True, message="OK, Returning data from Visualization's get method", data=data_linechart, status_code=200)
            
            elif graph_name == "scatter graph":
                
                column_name2 = data_from_json['column name 2']
                data_scatter = class_object.scattergraph(column_name1,column_name2)
                
                return getCustomResponse(success=True, message="OK, Returning data from Visualization's get method", data=data_scatter, status_code=200)
            
            elif graph_name == "data completeness":
                
                data_completeness = class_object.data_completeness()
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_completeness, status_code=200)
            
            
            elif graph_name == "heatmap full dataset":
                
                data_heatmap_full_dataset = class_object.heatmap_full_dataset()
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_heatmap_full_dataset, status_code=200)
            
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from Visualization's get method", data=None, status_code=400)
