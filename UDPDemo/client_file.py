#_*_coding:utf-8_*_
import socket

# 传输大文件。 UDP可能会有丢包，乱序等。

fileName = "recv.data"
BUFSIZ = 1024 * 5
count = 0 #接收次数
serverAddr = ('127.0.0.1', 8000)
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(client)
client.sendto("hello".encode('utf-8'), serverAddr)

# UDP存在丢包 乱序等。
with open(fileName, "wb") as f:
    while True:
        back_msg, addr = client.recvfrom(BUFSIZ)
        count += 1
        if len(back_msg) == 0: # 或者 if not back_msg:
            break
        print(count, len(back_msg),back_msg[:10])
        f.write(back_msg)
print("recv:",count) #包含最后一个空包/结束包。