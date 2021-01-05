# coding=utf-8
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 基于网络的数据报协议 UDP
server.bind(('0.0.0.0',8080)) # 127.0.0.1 只能接收局域网内的。 0.0.0.0 接收任何地方。

while True:
    msg,addr=server.recvfrom(1024)
    print(msg,addr)
    server.sendto(msg.upper(),addr)
