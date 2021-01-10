#_*_coding:utf-8_*_

import socket
# 测试丢包 乱序现象。

fileName = "recv.data"
BUFSIZ = 1024 * 5
count = 0 #接收次数
loss = 0 # 丢失次数
disorder = 0 # 乱序次数
id = 0
pre_id = 0
serverAddr = ('127.0.0.1', 8000)
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(client)

client.sendto("hello".encode('utf-8'), serverAddr)

# UDP存在丢包 乱序等。 验证丢包，乱序。
with open(fileName, "wb") as f:
    while True:
        back_msg, addr = client.recvfrom(BUFSIZ + 2)
        count += 1
        if len(back_msg) == 0: # 或者 if not back_msg:
            break
        print(count, len(back_msg),back_msg[:10])
        id = int.from_bytes(back_msg[:2], 'big')
        print(id)
        if(id != pre_id + 1):
            loss += id - pre_id - 1  # 丢包了。 丢包数
        if(id < pre_id):
            disorder +=1
        pre_id = id
        f.write(back_msg[2:])
# print("recv:",count) #包含最后一个空包/结束包。
#其实total不准确，因为有可能最后一个包时丢失的。 这里只是计算个大概。
print("total,recv, loss:",id + 1 , count, id + 1- count)
print("loss:", loss)
print("disorder:",disorder)