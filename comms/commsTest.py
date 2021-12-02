import comms
import time


testTable = { #all actions are to be logged in a table mapping the command to be sent to a function of the action to be taken, example below

    "volumeUp" : lambda : print('Running Volume Up'),
    "volumeDown" : lambda : print('Running Volume Down')

}


server = 'mqtt.eclipseprojects.io'
test1 = comms.mqttCommunicator(server, testTable)

test2 = comms.mqttCommunicator(server, testTable)

time.sleep(10)

test1.send_command("volumeUp")

while(1):
    pass
