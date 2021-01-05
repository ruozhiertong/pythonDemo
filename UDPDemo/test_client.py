#_*_coding:utf-8_*_

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(client)
while True:
    msg=input('>>: ').strip()
    if not msg:continue

    client.sendto(msg.encode('utf-8'),('120.229.91.63', 8080)) #18.197.196.35
    print(client)
    back_msg,addr=client.recvfrom(1024)
    print(back_msg.decode('utf-8'),addr)