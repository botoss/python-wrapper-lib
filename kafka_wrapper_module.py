# -*- coding: utf-8 -*-
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join('.')))
from in_message import InMessage
from out_message import OutMessage
from kafka import KafkaConsumer, KafkaProducer

class KafkaWrapperModule:
    
    def __init__(self, ip, port, in_topic, out_topic, command_list):
        self.ip = ip
        self.port = port
        self.in_topic = in_topic
        self.out_topic = out_topic
        self.command_list = command_list

        print(self)

        try:
            self.producer = KafkaProducer(bootstrap_servers=':'.join([ip, port]))
        except Exception as e:
            print "Error 1"
            print e.message
            sys.exit(-1)

        try:
            self.consumer = KafkaConsumer(bootstrap_servers=':'.join([ip, port]), auto_offset_reset='earliest')
            self.consumer.subscribe([self.in_topic])
        except Exception as e:
            print "Error 2"
            print e.message
            sys.exit(-1)

    def wait_for_command(self, command_list):
        for message in self.consumer:
            print('input raw message', message)
            in_message = InMessage(key=message.key, json_data=json.loads(message.value))
            if in_message.command in command_list:
                self.process_command(in_message)

    def process_command(self, in_message):
        result = self.handle_command(in_message)
        self.send_result(result)

    def handle_command(self, in_message):
        print('Implement me!!!')
    
    def send_result(self, out_message):
        self.producer.send(topic=self.out_topic, value=out_message.toJson(), key=out_message.key)
        self.producer.flush()

    def start(self):
        print('start')
        self.wait_for_command(self.command_list)

    def __str__(self):
        str = '===============================================================================\n'
        str += "KafkaWrapperModule\n"
        str += "ip: " + self.ip + "\n"
        str += "port: " + self.port + "\n"
        str += "in_topic: " + self.in_topic + "\n"
        str += "out_topic: " + self.out_topic + "\n"
        str += "command_list: " + ','.join(self.command_list) + "\n"
        str += '===============================================================================\n'
        return str
