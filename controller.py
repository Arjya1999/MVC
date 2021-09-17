from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *
from helper import *
from data_visualization import DataVisualization

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
        
            results = var.update(data_request_json['ids'], data_request_json['name'], data_request_json['Age'], data_request_json['gender'])

            return getCustomResponse(success=True, message="OK, Returning data from RecordHandling's put method", data = results['message'], status_code=200)            
        except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from RecordHandling's put method", data=None, status_code=400)


class Visualization(Resource):
    
    def get(self):
        #try:
            class_object = DataVisualization()
            data_from_json = request.get_json()
            graph_name= data_from_json["graph_name"].lower()
            
            try:
                column_name1 = data_from_json['column_name1']
            except:
                pass

            if graph_name == "histogram":
                data_histogram = class_object.histogram(column_name1)
                
                with open('assets/histogram.json') as f:
                    graph_template_histogram = json.load(f)
                    
                graph_template_histogram["series"][1].update({"data":data_histogram['x_data']})
                graph_template_histogram["title"].update({"text":"Histogram of "+column_name1})
                graph_template_histogram["xAxis"][0]['title'].update({"text":column_name1})
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= graph_template_histogram, status_code=200)
            
            if graph_name == "boxplot":
                data_histogram = class_object.histogram(column_name1)
                
                with open('assets/boxplot.json') as f:
                    graph_template_boxplot = json.load(f)
                    
                    graph_template_boxplot["series"][0].update({"data":[data_histogram['x_data']]})
                    graph_template_boxplot["xAxis"].update({"categories":column_name1})
                    graph_template_boxplot["xAxis"]['title'].update({"text":column_name1})
                    graph_template_boxplot["title"].update({"text":"Boxplot of "+column_name1})

                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= graph_template_boxplot, status_code=200)

            elif graph_name == "pie chart":
                
                data_pie_chart = class_object.pie_chart(column_name1)
                with open('assets/pie_chart.json') as f:
                        graph_template_data_pie_chart = json.load(f)
                
                graph_template_data_pie_chart["series"][0].update({"data":data_pie_chart})
                graph_template_data_pie_chart["title"].update({"text":"Pie chart for column "+column_name1})

                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= graph_template_data_pie_chart, status_code=200)
            
            elif graph_name == "graph distribution":
            
                data_graph_distribution = class_object.graph_distribution(column_name1)
                with open('assets/graph_distribution.json') as f:
                    graph_template_bell_curve = json.load(f)
                 
                graph_template_bell_curve["series"][1].update({"data":data_graph_distribution['x_data']})
                graph_template_bell_curve["title"].update({"text":"Data Distribution of "+column_name1})
                graph_template_bell_curve["xAxis"][0]['title'].update({"text":column_name1})
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= graph_template_bell_curve, status_code=200)
            
            elif graph_name == "graph for column relation with target variable":
            
                data_correlation_with_target_variable = class_object.graph_for_column_relation_with_target_variable(column_name1)
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_correlation_with_target_variable, status_code=200)
            
            elif graph_name == "bar graph":
            
                data_bar_graph = class_object.Bargraph(column_name1)
                with open('assets/categories_and_their_counts.json') as f:
                    graph_template_value_counts = json.load(f)
                    
                graph_template_value_counts["series"][0].update({"data":data_bar_graph['y_data']})
                graph_template_value_counts["xAxis"].update({"categories":data_bar_graph['x_data']})

                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= graph_template_value_counts, status_code=200)
                        
            elif graph_name == "line chart":
                
                column_name2 = data_from_json['column_name2']
                data_linechart = class_object.linechart(column_name1,column_name2)
                
                return getCustomResponse(success=True, message="OK, Returning data from Visualization's get method", data=data_linechart, status_code=200)
            
            elif graph_name == "scatter graph":
                
                column_name2 = data_from_json['column_name2']
                data_scatter = class_object.scattergraph(column_name1,column_name2)
                
                with open('assets/scatter_plot.json') as f:
                    graph_template_scatter_plot = json.load(f)
                    
                graph_template_scatter_plot["series"][0].update({"data":data_scatter['x_data']})
                graph_template_scatter_plot["series"][0].update({"name":"Data points"})
                graph_template_scatter_plot["title"].update({"text":"Scatter graph of "+column_name1+" and "+column_name2})
                graph_template_scatter_plot["xAxis"]['title'].update({"text":column_name1})
                graph_template_scatter_plot["yAxis"]['title'].update({"text":column_name2})

                return getCustomResponse(success=True, message="OK, Returning data from Visualization's get method", data=graph_template_scatter_plot, status_code=200)
            
            elif graph_name == "data completeness":
                
                data_completeness = class_object.data_completeness()
                
                with open('assets/data_completeness.json') as f:
                    graph_template_data_competeness = json.load(f)
                    
                graph_template_data_competeness["series"][0].update({"data":data_completeness['y_data']})
                graph_template_data_competeness["xAxis"].update({"categories":data_completeness['x_data']})
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= graph_template_data_competeness, status_code=200)
            
            elif graph_name == "heatmap full dataset":
                
                data_heatmap_full_dataset = class_object.heatmap_full_dataset()
                
                return getCustomResponse(success=True, message="OK, Returning data from Histogram's get method", data= data_heatmap_full_dataset, status_code=200)
            
        #except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from Visualization's get method", data=None, status_code=400)
