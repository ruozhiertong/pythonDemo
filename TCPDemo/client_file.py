#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 9000
BUFSIZ = 10240
ADDRESS = (HOST, PORT)
fileName = "recv.mp4"

tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientSocket.connect(ADDRESS)

with open(fileName, "wb") as f:
    while True:
        # 接收数据
        data, ADDR = tcpClientSocket.recvfrom(BUFSIZ)
        print(len(data))
        if not data:
            break
        f.write(data)

print("链接已断开！")
tcpClientSocket.close()