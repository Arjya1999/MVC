
from flask import Flask
from flask_restx import Api
from controller import *
from config import ConfigProduction

app=Flask('__name__')
app.config.from_object('config.ConfigProduction')

api=Api(app)

api.add_resource(RecordHandling, '/records')
api.add_resource(Histogram, '/histogram')

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])
