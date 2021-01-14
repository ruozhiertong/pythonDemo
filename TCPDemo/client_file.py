#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 9000
BUFSIZ = 10240 * 5
ADDRESS = (HOST, PORT)
fileName = "recv.mp4"

recv_time = 0
recv_total = 0

tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientSocket.connect(ADDRESS)

with open(fileName, "wb") as f:
    while True:
        # 接收数据
        data, ADDR = tcpClientSocket.recvfrom(BUFSIZ)
        print(len(data))
        recv_time += 1
        recv_total += len(data)
        if not data:
            break
        f.write(data)

print("链接已断开！")
tcpClientSocket.close()

print(recv_time, recv_total)