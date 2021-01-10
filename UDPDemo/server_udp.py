# coding=utf-8
import socket
# 测试丢包 乱序现象。
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 基于网络的数据报协议 UDP
server.bind(('0.0.0.0',8000)) # 127.0.0.1 只能接收局域网内的。 0.0.0.0 接收任何地方。
fileName = "../TCPDemo/data.mp4"
BUFSIZ = 1024 * 5

count = 0 #发送次数
# server.settimeout(5) #设置超时
# 接收客户端。会一直阻塞。 可以设置超时。
msg, addr = server.recvfrom(1024)
print(msg, addr)
with open(fileName, "rb") as f:
    sendData = f.read(BUFSIZ)  # 10k
    while len(sendData) != 0:  # ==0 时结束文件读取。
        count += 1
        server.sendto(count.to_bytes(2,byteorder='big') + sendData, addr) #5122
        print(count, len(sendData))
        sendData = f.read(BUFSIZ)  # 10k

# 告诉客户端结束了。否则客客户端会傻傻等待 recvfrom。 因为不像TCP那样可以有close，所以这里自己send一个空的过去
count +=1
server.sendto(sendData,addr) # server.sendto(b'',addr)
print(count) # 包含最后一个空包/结束包。