import socket

TransportLayerProtocol = 0         # 传输层协议 TCP = 0 / UDP = 1
Host = 'xxx.xxx.xxx.xxx'            # 服务器IP
Port = 9090                        # 服务器端口号
IPVersion = 1                      # IP协议的版本 IPv4 = 0 / IPv6 = 1
Backlog = 5                        # 拒绝连接之前，可以挂起的最大连接数量
Bufsize = 1024                     # 指定最多可以接收的字节数

if(TransportLayerProtocol == 0):
    # 创建服务端的socket对象SocketServer
    if(IPVersion == 0):
        SocketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        SocketServer = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    SocketServer.bind((Host, Port))  # 绑定服务器IP及端口
    SocketServer.listen(Backlog)  # 设置监听
    # 等待客户端的连接

    clientsocket, address = SocketServer.accept()
    # 当有连接时候返回的参数1为客户端的socket对象，参数2为客户端的地址(IP地址，端口号)

    while True:
        # 接收客户端的请求
        recvmsg = clientsocket.recv(Bufsize)
        # 把接收到的数据进行解码
        strData = recvmsg.decode("utf-8")
        print("收到:" + strData)
        # 接受成功回复消息
        msg = "I am TCP with " + str(IPVersion)
        # 对要发送的数据进行编码
        clientsocket.send(msg.encode("utf-8"))

    SocketServer.close()  # 关闭连接

else:
    # 创建服务端的socket对象SocketServer
    if(IPVersion == 0):
        SocketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        SocketServer = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    SocketServer.bind((Host, Port))  # 设置监听
    while True:
        # 调用接受消息
        recvmsg, address = SocketServer.recvfrom(Bufsize)
        # 把接收到的数据进行解码
        strData = recvmsg.decode("utf-8")
        print("收到:" + strData)
        # 接受成功回复消息
        msg = "I am UDP with "+str(IPVersion)
        SocketServer.sendto(msg.encode("utf-8"), address)

    SocketServer.close()  # 关闭连接接
