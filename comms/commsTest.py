import comms
import time


testTable = { #all actions are to be logged in a table mapping the command to be sent to a function of the action to be taken, example below

    "volumeUp" : lambda : print('Running Volume Up'),
    "volumeDown" : lambda : print('Running Volume Down')

}


server = 'test.mosquitto.org'
test1 = comms.mqttCommunicator(server, testTable)

time.sleep(3)

test1.send_command("power")
time.sleep(12)
test1.send_command("volumeUp")
time.sleep(2)
test1.send_command("volumeDown")
time.sleep(2)
test1.send_command("channelUp")
time.sleep(2)
test1.send_command("channelDown")



while(1):
    time.sleep(2)
    test1.send_command("volumeUp")

    pass
