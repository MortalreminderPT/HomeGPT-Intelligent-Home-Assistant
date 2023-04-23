from flask_restful import Resource

from dao.devicestates import device_states

class ArduinoApi(Resource):
    def get(self):
        return device_states.get()