import paho.mqtt.client as mqtt
import numpy as np
import json
import time


class mqttCommunicator:

    topic = 'airpower'

    def __init__(self, server : str, actionTable: dict): #action table is a string -> function dictionary
        self.actionTable = actionTable
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.client.on_message = self.on_message
        self.client.connect_async(server)
        self.client.loop_start()

    #debugging/logging function
    def on_connect(self, client, userdata, flags, rc):
        print("Connection returned result: "+str(rc))
   
   
    #debugging/logging function
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print('Unexpected Disconnect')
        else:
            print('Expected Disconnect')


    #internal on_message function
    def on_message(self, client, userdata, message):
        #TODO: verify topic is correct
        decodedMessage = json.loads(message.payload)
        if "command" in decodedMessage:
            command = decodedMessage["command"]
        else:
            print('Message Error: Received message: "' + str(message.payload) + '" on topic "' +
                message.topic + '" with QoS ' + str(message.qos))
            return
        if command in self.actionTable:
            action = self.actionTable[command]
            action()
        else:
            print('Command Error: Received message: "' + str(message.payload) + '" on topic "' +
                message.topic + '" with QoS ' + str(message.qos))
            return
       
        print('Action Successful: Received message: "' + str(message.payload) + '" on topic "' +
            message.topic + '" with QoS ' + str(message.qos))
    
    #generic send message function if needed, preferrably use send_command though for basic command publishing
    def send_message(self, message: str):
        self.client.publish(self.topic, message, qos=1)

    def send_command(self, command: str):
        payload = {
            "command" : command,
            "timestamp" : time.time()
        }
        
        self.client.publish(self.topic, json.dumps(payload), qos=1)

    


#commands are sent in the form of JSON strings, which have at least an element {"command": "someCommand"}. 

#perhaps adding timestamps or something else to the json string would be wise but the code works with or without it

exampleActionTable = { #all actions are to be logged in a table mapping the command to be sent to a function of the action to be taken, example below

    "volumeUp" : lambda : print('Running Volume Up'),
    "volumeDown" : lambda : print('Running Volume Down')

}