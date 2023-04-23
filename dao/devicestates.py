from typing import Dict, Any
import pymongo
import config

client = pymongo.MongoClient(config.MONGO_URI)
db = client['arduino']
possible_devices = db['possible_devices']
devices = db['device']

DeviceState = Dict[str, Dict[str, Any]]

class DeviceStates(object):
    def __init__(self):
        self.state = {}
        self._flash = False
        pass

    def get(self):
        if not self._flash:
            self._flash = True
            for device_state in list(devices.find(projection = {'_id': 0})):
                self.state[device_state['device']] = device_state
        return self.state

    def update(self, update_dict:DeviceState):
        for update_device, update_state in update_dict.items():
            devices.update_one({f'_id':update_device}, {'$set':{**update_state}}, upsert=True)
            self.state[update_device] = update_state
        return self.get()

    def delete(self, all = True):
        self.state = {}
        return devices.delete_many({}).deleted_count

device_states = DeviceStates()