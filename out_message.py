# -*- coding: utf-8 -*-
import json

class OutMessage:

    def __init__(self, key, connector_id=None, text=None, json_data=None):
        self.key = key
        if json_data:
            self.fromJson(json_data)
        else:
            self.connector_id = connector_id
            self.text = text

        print(self)

    def toJson(self):
        return json.dumps({"connector-id": self.connector_id, "text": self.text})

    def fromJson(self, json_data):
        if 'connector-id' in json_data:
            self.connector_id = json_data['connector-id'].encode('utf-8')
        if 'text' in json_data:
            self.text = json_data['text'].encode('utf-8')

        if not hasattr(self, 'connector_id'):
            self.connector_id = 'none'
        if not hasattr(self, 'text'):
            self.text = 'none'
    
    def __str__(self):
        str = '===============================================================================\n'
        str += "OutMessage\n"
        str += "key: " + self.key + "\n"
        str += "connector_id: " + self.connector_id + "\n"
        str += "text: " + self.text + "\n"
        str += '===============================================================================\n'
        return str
