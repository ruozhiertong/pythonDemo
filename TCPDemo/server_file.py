import socket


# 编码过程和c socket类似。
HOST = ''
PORT = 9000
BUFSIZ = 102 #1024*10
ADDRESS = (HOST, PORT)
fileName = "data.mp4"
# 创建监听socket
tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和固定端口
tcpServerSocket.bind(ADDRESS)
print("服务器启动，监听端口{}...".format(ADDRESS[1]))

tcpServerSocket.listen(5)#5 连接数。

send_time = 0

total_send = 0

try:
    while True:
        print('服务器正在运行，等待客户端连接...')

        # client_socket是专为这个客户端服务的socket，client_address是包含客户端IP和端口的元组
        client_socket, client_address = tcpServerSocket.accept()
        print('客户端{}已连接！'.format(client_address))
        total_send = 0
        send_time = 0
        try:
            with open(fileName,"rb") as f:
                # read对于b类型读取的都是二进制数据，而对于其他则读取的都是字符串。
                sendData = f.read(BUFSIZ)  # 10k
                while len(sendData) != 0 and send_time < 10: # ==0 时结束文件读取。
                    print(len(sendData))
                    send_len = client_socket.send(sendData)
                    print(send_len)
                    total_send += send_len
                    send_time += 1
                    sendData = f.read(BUFSIZ)  # 10k
        finally:
            # 关闭为这个客户端服务的socket
            client_socket.close()
            print(total_send)
finally:
    # 关闭监听socket，不再响应其它客户端连接
    tcpServerSocket.close()