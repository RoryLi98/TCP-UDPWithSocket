import socket

TransportLayerProtocol = 0         # 传输层协议 TCP = 0 / UDP = 1
Host = '220.181.38.148'            # 服务器IP 
Port = 9090                        # 服务器端口号
IPVersion = 1                      # IP协议的版本 IPv4 = 0 / IPv6 = 1
Backlog = 5                        # 拒绝连接之前，可以挂起的最大连接数量
Bufsize = 1024                     # 指定最多可以接收的字节数

if(TransportLayerProtocol == 0):
    #创建服务端的socket对象SocketClient
    if(IPVersion == 0):
        SocketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        SocketClient = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    SocketClient.connect((Host, Port))    #建立连接
  
    while True:
        msg = "I am TCP Sender with "+str(TransportLayerProtocol)  
        SocketClient.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
        data = SocketClient.recv(Bufsize ) #接收一个信息，并指定接收的大小 为1024字节
        print('recv:',data.decode("utf-8")) #输出我接收的信息
        
    SocketClient.close()

else:
    #创建服务端的socket对象SocketClient
    if(IPVersion == 0):
        SocketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        SocketClient = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    while True:
        msg = "I am UDP Sender with "+str(TransportLayerProtocol)
        SocketClient.sendto(msg.encode("utf-8"),(Host,Port))
        data = SocketClient.recv(Bufsize ) #接收一个信息，并指定接收的大小 为1024字节
        print('recv:',data.decode("utf-8")) #输出我接收的信息

    SocketClient.close()    #关闭链接
