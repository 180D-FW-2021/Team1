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

def command(str, count=1):
    #command = "irsend SEND_ONCE " + remote + " " + str
    #os.system(command)
    if count == 1:
      lircClient.send_once(remote, str)
    else:
      lircClient.send_once(remote, str, repeat_count = count-1 )
    print("Recieved a " + str + "and count " + str(count), ", running ")

actionTable = {

    "volumeUp" : lambda count: command("KEY_VOLUMEUP", count),
    "volumeDown" : lambda count: command("KEY_VOLUMEDOWN", count),
    "power" : lambda count: command("KEY_POWER", count),
    "channelUp" : lambda count: command("KEY_CHANNELUP", count),
    "channelDown" : lambda count: command("KEY_CHANNELDOWN", count),
    "0": lambda count : command("KEY_0", count),
    "1": lambda count : command("KEY_1", count),
    "2": lambda count : command("KEY_2", count),
    "3": lambda count : command("KEY_3", count),
    "4": lambda count : command("KEY_4", count),
    "5": lambda count : command("KEY_5", count),
    "6": lambda count : command("KEY_6", count),
    "7": lambda count : command("KEY_7", count),
    "8": lambda count : command("KEY_8", count),
    "9": lambda count : command("KEY_9", count),
}

reciever = comms.mqttCommunicator(config.mqttServer, actionTable, config.mqttTopic, subscribe=True)

reciever.loop_forever()
