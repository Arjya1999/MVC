
from flask import Flask
from flask_restx import Api
from controller import *

app=Flask('__name__')

api=Api(app)

api.add_resource(RecordHandling, '/records')

if __name__ == '__main__':
    app.run(debug=True)
