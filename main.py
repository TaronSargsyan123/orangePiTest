import argparse

import serial
import socket
import time

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=8000, help="Running port")
parser.add_argument("-i", "--ip", type=str, default='192.168.1.2', help="Ip address")
parser.add_argument('-s', '--serial', type=str, default='/dev/ttyUSB0', help="Serial port")
args = parser.parse_args()

port = args.port
host = args.host
listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serialcomm = serial.Serial(args.serial, 9600)
serialcomm.timeout = 1

def sendMessage(temp):
    serialcomm.write(temp.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))

try:
    listensocket.bind((host, port))
    listensocket.listen(999)
    sendMessage(str(host))
    print("Server started at " + host + " on port " + str(port))
except:
    sendMessage(str("invalid host"))
    print("invalid host")

sendMessage(str(host))
running = True
sendMessage(str(host))

while running:
    sendMessage(str(host))
    (clientsocket, address) = listensocket.accept()
    print("New connection made! address = " + str(address))


    message = clientsocket.recv(1024).decode()
    print("message is: " + message)

    if message == "on":
        sendMessage("on")
    elif message == "off":
        sendMessage("off")
    elif message == "left":
        sendMessage(str(host))
    elif message == "clear":
        pass
    elif message == "close":
        clientsocket.close()
        running = False