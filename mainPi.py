import time
import comms.comms as comms #fix this, in comms put __init__.py to import comms, but rename comms.py to mqttCommunicator.py, will break other code for now so do later
import os
import socket
import lirc
import config


lircClient = lirc.Client(
  connection=lirc.LircdConnection(
    address="/var/run/lirc/lircd",
    socket=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM),
    timeout = 5.0
  )
)


remote = config.defaultRemote
#may add functionality to change remote during operation later, so keeping this

def command(str):
    #command = "irsend SEND_ONCE " + remote + " " + str
    #os.system(command)
    lircClient.send_once(remote, str)
    print("Recieved a " + str + ", running ")

actionTable = {

    "volumeUp" : lambda : command("KEY_VOLUMEUP"),
    "volumeDown" : lambda : command("KEY_VOLUMEDOWN"),
    "power" : lambda : command("KEY_POWER"),
    "channelUp" : lambda : command("KEY_CHANNELUP"),
    "channelDown" : lambda : command("KEY_CHANNELDOWN"),
    "0": lambda : command("KEY_0"),
    "1": lambda : command("KEY_1"),
    "2": lambda : command("KEY_2"),
    "3": lambda : command("KEY_3"),
    "4": lambda : command("KEY_4"),
    "5": lambda : command("KEY_5"),
    "6": lambda : command("KEY_6"),
    "7": lambda : command("KEY_7"),
    "8": lambda : command("KEY_8"),
    "9": lambda : command("KEY_9"),
}

reciever = comms.mqttCommunicator(config.mqttServer, actionTable, config.mqttTopic)

reciever.loop_forever()
