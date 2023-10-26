from colormath.color_objects import sRGBColor, CMYKColor
from colormath.color_conversions import convert_color
import configparser
import serial
import socket
import time
import json

config = configparser.ConfigParser()
config.read("./conf.conf")

with open("color_table.json", "r") as f:
    colors = json.load(f)

ser = serial.Serial(
    port="/dev/cu.usbmodem1401",
    baudrate=9600
)
print(ser.readline().decode().replace("\r\n", ""))  # Hi


def send_color(R, Y, B, P):
    ser.write("b".encode('utf-8'))

    ser.write(str(R).encode('utf-8'))
    print(ser.readline().decode().replace("\r\n", ""))

    ser.write(str(Y).encode('utf-8'))
    print(ser.readline().decode().replace("\r\n", ""))

    ser.write(str(B).encode('utf-8'))
    print(ser.readline().decode().replace("\r\n", ""))

    ser.write(str(P).encode('utf-8'))
    print(ser.readline().decode().replace("\r\n", ""))

    return ser.readline().decode().replace("\r\n", "")


def rgb_to_cmyk(r, g, b):
    # RGB 값을 sRGBColor 객체로 변환
    rgb_color = sRGBColor(r, g, b)

    # CMYK로 변환
    cmyk_color = convert_color(rgb_color, CMYKColor)

    # 각 색상 구성 요소를 가져옴
    c = cmyk_color.cyan
    m = cmyk_color.magenta
    y = cmyk_color.yellow
    k = cmyk_color.key

    return c, m, y, k


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((config['DEFAULT']['addr'], int(config['DEFAULT']['port'])))
print("Server listening...")
soc.listen(1)
server, addr = soc.accept()
print(f"Connection established with {addr}")

while True:
    try:
        data = json.loads(server.recv(256))
    except json.decoder.JSONDecodeError:
        server.close()
        exit(0)  # Illegal data

    R, Y, B, P = colors[data['code']]

    total_time = 3000
    margin = 700

    R = total_time * R / 100 + margin if not R == 0 else 0
    Y = total_time * Y / 100 + margin if not Y == 0 else 0
    B = total_time * B / 100 + margin if not B == 0 else 0
    P = total_time * P / 100 + margin if not P == 0 else 0

    suc = int(send_color(R, Y, B, P))

    if suc == 1:
        server.send(json.dumps({
            "_id": data["_id"],
            "status": "done",
            "device": config['DEFAULT']['deviceName']
        }).encode())

    else:
        server.send(json.dumps({
            "_id": data["_id"],
            "status": "error",
            "device": config['DEFAULT']['deviceName']
        }).encode())
