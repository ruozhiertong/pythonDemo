import socket


# 编码过程和c socket类似。
HOST = ''
PORT = 9000
BUFSIZ = 10240
ADDRESS = (HOST, PORT)
fileName = "data.mp4"
# 创建监听socket
tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和固定端口
tcpServerSocket.bind(ADDRESS)
print("服务器启动，监听端口{}...".format(ADDRESS[1]))

tcpServerSocket.listen(5)#5 连接数。

try:
    while True:
        print('服务器正在运行，等待客户端连接...')

        # client_socket是专为这个客户端服务的socket，client_address是包含客户端IP和端口的元组
        client_socket, client_address = tcpServerSocket.accept()
        print('客户端{}已连接！'.format(client_address))

        try:
            with open(fileName,"rb") as f:
                # read对于b类型读取的都是二进制数据，而对于其他则读取的都是字符串。
                sendData = f.read(BUFSIZ)  # 10k
                while len(sendData) != 0: # ==0 时结束文件读取。
                    print(len(sendData))
                    client_socket.send(sendData)
                    sendData = f.read(BUFSIZ)  # 10k
        finally:
            # 关闭为这个客户端服务的socket
            client_socket.close()
finally:
    # 关闭监听socket，不再响应其它客户端连接
    tcpServerSocket.close()