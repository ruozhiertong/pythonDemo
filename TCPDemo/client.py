#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 12900
BUFSIZ = 1024
ADDRESS = (HOST, PORT)

tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientSocket.connect(ADDRESS)

while True:
    data = input('>')
    if not data:
        break
    # print(type(data))
    # print(len(data))
    data += '\n'
    # print(type(data))
    # print(len(data))
    #发送数据
    tcpClientSocket.send(data.encode('utf-8'))
    # 接收数据
    data, ADDR = tcpClientSocket.recvfrom(BUFSIZ)
    if not data:
        break
    print("服务器端响应：", data.decode('utf-8'))

print("链接已断开！")
tcpClientSocket.close()