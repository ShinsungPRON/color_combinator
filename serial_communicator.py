import configparser
import time
import json
import serial
import socket

config = configparser.ConfigParser()
config.read("./conf.conf")

ser = serial.Serial(
    port=config['DEFAULT']['serialPort'],
    baudrate=9600
)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((config['DEFAULT']['addr'], int(config['DEFAULT']['port'])))
soc.listen(1)

server, addr = soc.accept()

while True:
    data = server.recv(256)

    ser.write(data['code'])

    while not ser.readable():
        time.sleep(0.1)

    suc = ser.read()

    soc.send(json.dumps({
        "_id": data["_id"],
        "status": "done",
        "device": config['DEFAULT']['deviceName']
    }).encode())