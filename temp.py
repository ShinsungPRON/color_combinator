import socket
import json

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", 5000))

while True:
    code = input().replace('\n', '').strip()

    soc.send(json.dumps({
        "_id": "ashibalsex",
        "code": code
    }).encode())

    data = soc.recv(1024)
    print(data.decode())