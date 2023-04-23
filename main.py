from flask import Flask
import flask_restful as restful
from flask_pymongo import PyMongo

import config
from api.arduino import ArduinoApi
from api.order import OrderApi

app = Flask(__name__)
api = restful.Api(app, default_mediatype="application/json")
api.add_resource(OrderApi, '/')
api.add_resource(ArduinoApi, '/arduino')

mongo = PyMongo(app, uri=config.MONGO_URI)

if __name__ == '__main__':
    app.run()