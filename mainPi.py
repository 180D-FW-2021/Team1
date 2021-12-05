import os
import time
import comms

actionTable = {

    "volumeUp" : lambda : os.system("irsend SEND_ONCE UR5U-8790L-TWC KEY_VOLUMEUP"),
    "volumeDown" : lambda : os.system("irsend SEND_ONCE UR5U-8790L-TWC KEY_VOLUMEDOWN"),
    "power" : lambda : os.system("irsend SEND_ONCE UR5U-8790L-TWC KEY_POWER"),
    "channelUp" : lambda : os.system("irsend SEND_ONCE UR5U-8790L-TWC KEY_CHANNELUP"),
    "channelDown" : lambda : os.system("irsend SEND_ONCE UR5U-8790L-TWC KEY_CHANNELDOWN")

}


server = 'mqtt.eclipseprojects.io'

reciever = comms.mqttCommunicator(server, actionTable)