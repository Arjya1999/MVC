from flask import Flask, jsonify,request
from flask_restx import Resource
from model import *

class RecordHandling(Resource):
    global var
    var=DataHandling()
    def get(self):
        ids = request.args.getlist('ids')
        print(ids)
        if ids== []:
            try:
                display_all_records= var.display()
                return jsonify({"status":200,"message":"OK, Returning data from get method","data": display_all_records})
            except:
                return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method","data":[]})
        else:
            try:
                display_record_by_id= var.display_by_id(ids[0])
                return jsonify({"status":200,"message":"OK, Returning data from get method","data": display_record_by_id})
            except:
                return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method","data":[]})
    
    def post(self):
        name = request.args.getlist('name')
        Age = request.args.getlist('Age')
        gender = request.args.getlist('gender')
        try:
            result=var.add({"name":name[0],"Age":Age[0],"gender":gender[0]})
            return jsonify({"status":200,"message":"OK, Returning data from post method","data": result})
        except:
            return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from post method","data":[]})
        
    def delete(self):
        ids= request.args.getlist('ids')
        try:
            info=var.delete(ids[0])
            return jsonify({"status":200,"message":"OK, Returning data from delete method","data": info})
        except:
            return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from delete method","data":[]})

    def put(self):
        ids= request.args.getlist('ids')
        name = request.args.getlist('name')
        Age = request.args.getlist('Age')
        gender = request.args.getlist('gender')
        try:
            result=var.update(ids[0],name[0],Age[0],gender[0])
            return jsonify({"status":200,"message":"OK, Returning data from put method","data": result})
        except:
            return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from put method","data":[]})