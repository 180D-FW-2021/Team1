
import time
import comms.comms as comms
import os
import socket
import lirc


lircClient = lirc.Client(
  connection=lirc.LircdConnection(
    address="/var/run/lirc/lircd",
    socket=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM),
    timeout = 5.0
  )
)

remote = "UR5U-8790L-TWC"



def command(str):
    command = "timeout -s SIGINT 0.3 irsend SEND_ONCE UR5U-8790L-TWC " + str
    os.system(command)
    #lircClient.send_once(remote, str)
    print("Recieved a " + str + ", running ")

actionTable = {

    "volumeUp" : lambda : command("KEY_VOLUMEUP"),
    "volumeDown" : lambda : command("KEY_VOLUMEDOWN"),
    "power" : lambda : command("KEY_POWER"),
    "channelUp" : lambda : command("KEY_CHANNELUP"),
    "channelDown" : lambda : command("KEY_CHANNELDOWN"),

}


server = 'mqtt.eclipseprojects.io'

reciever = comms.mqttCommunicator(server, actionTable)

while(1):
    pass
