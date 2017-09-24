# -*- coding: utf-8 -*-
import json

class InMessage:

    def __init__(self, key, connector_id=None, command=None, params=None, json_data=None):
        self.key = key
        if json_data:
            self.fromJson(json_data)
        else:
            self.connector_id = connector_id
            self.command = command
            self.params = params

        print(self)
        
    def toJson(self):
        return json.dumps({"connector-id": self.connector_id, "command": self.command, "params": self.params})

    def fromJson(self, json_data):
        if 'connector-id' in json_data:
            self.connector_id = json_data['connector-id'].encode('utf-8')
        if 'command' in json_data:
            self.command = json_data['command'].encode('utf-8')
        if 'params' in json_data:
            self.params = [param.encode('utf-8') for param in json_data['params']]

        if not hasattr(self, 'connector_id'):
            self.connector_id = 'none'
        if not hasattr(self, 'command'):
            self.command = 'none'
        if not hasattr(self, 'params'):
            self.params = 'none'

    def __str__(self):
        output = '===============================================================================\n'
        output += "InMessage\n"
        output += "key: " + self.key + "\n"
        output += "connector_id: " + self.connector_id + "\n"
        output += "command: " + self.command + "\n"
        output += "params: " + ','.join(self.params) + "\n"
        output += '===============================================================================\n'
        return output
