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
                display= var.display()
                return jsonify({"status":200,"message":"OK, Returning data from get method","data": display})
            except:
                return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method"})
        else:
            try:
                display= var.display_by_id(ids[0])
                return jsonify({"status":200,"message":"OK, Returning data from get method","data": display})
            except:
                return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method"})
    
    def post(self):
        name = request.args.getlist('name')
        Age = request.args.getlist('Age')
        gender = request.args.getlist('gender')
        try:
            result=var.add({"name":name[0],"Age":Age[0],"gender":gender[0]})
            return jsonify({"status":200,"message":"OK, Returning data from post method","data": result})
        except:
            return jsonify({"status":400, "message":"Bad Request, Some error has occured while returning data from get method"})
        
    def delete(self):
        ids= request.args.getlist('ids')
        info=var.delete(ids[0])
        return jsonify({"status":200,"message":"OK, Returning data from get method","data": info})

    def put(self):
        ids= request.args.getlist('ids')
        name = request.args.getlist('name')
        Age = request.args.getlist('Age')
        gender = request.args.getlist('gender')
        result=var.update(ids[0],name[0],Age[0],gender[0])
        return jsonify({"status":200,"message":"OK, Returning data from put method","data": result})