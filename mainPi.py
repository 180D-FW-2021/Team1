import os
import time
import comms


def command(str):
    os.system("irsend SEND_ONCE UR5U-8790L-TWC KEY " + str)
    print("Recieved a " + str + " command")

actionTable = {

    "volumeUp" : lambda : command("KEY_VOLUMEUP"),
    "volumeDown" : lambda : command("KEY_VOLUMEDOWN"),
    "power" : lambda : command("KEY_POWER"),
    "channelUp" : lambda : command("KEY_CHANNELUP"),
    "channelDown" : lambda : command("KEY_CHANNELDOWN"),

}


server = 'mqtt.eclipseprojects.io'

reciever = comms.mqttCommunicator(server, actionTable)