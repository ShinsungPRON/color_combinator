import configparser
import time
import json
import serial
import socket

config = configparser.ConfigParser()
config.read("./conf.conf")

with open("color_table.json", "r") as f:
    colors = json.load(f)

ser = serial.Serial(
    port=config['DEFAULT']['serialPort'],
    baudrate=9600
)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((config['DEFAULT']['addr'], int(config['DEFAULT']['port'])))
soc.listen(1)

server, addr = soc.accept()

while True:
    data = json.loads(server.recv(256))

    R, Y, B, P = colors[data['code']]

    ser.write("begin")
    ser.write(R)
    ser.write(Y)
    ser.write(B)
    ser.write(P)

    while not ser.readable():
        time.sleep(0.1)

    suc = ser.read()

    if suc == 'done':
        soc.send(json.dumps({
            "_id": data["_id"],
            "status": "done",
            "device": config['DEFAULT']['deviceName']
        }).encode())

    else:
        soc.send(json.dumps({
            "_id": data["_id"],
            "status": "error",
            "device": config['DEFAULT']['deviceName']
        }).encode())
