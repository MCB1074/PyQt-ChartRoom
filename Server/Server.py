from socket import *
from serverConfig import *
import threading

def recvMsg(client):
    msg = client.recv(1024).decode('utf-8')
    if msg != '':
        print('Client : ' + msg)
    return msg

def sendMsg(client,msg):
    client.send(msg.encode('utf-8'))
    print('Server : ' + msg)

def sendInputMsg(client):
    msg = input()
    client.send(msg.encode('utf-8'))

# 获取本机ip
s = socket(AF_INET, SOCK_DGRAM)
s.connect(('baidu.com', 0))
host = s.getsockname()[0]

print(host)

port = 8888

# 建立服务器
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口可立即重用
s.bind((host, port))    # 开启对应端口
s.listen(30)            # 最大连接数

usrnameToConn = {}      # 用户名对应的连接
clientsList = []        # 已连接用户的用户名
clientsNum = 0          # 已连接用户数

# 服务器输入指令
def broadcastOrder(order):
    for name in clientsList:
        conn = usrnameToConn[name]
        sendMsg(conn,'order')
        recvMsg(conn)
        sendMsg(conn,order)

def delusr(usrname):
    global clientsNum
    clientsList.remove(usrname)
    usrnameToConn[usrname].close()
    del usrnameToConn[usrname]
    clientsNum -= 1

def broadcastMsg(msg):
    for name in clientsList:
        conn = usrnameToConn[name]
        sendMsg(conn,'msg')
        recvMsg(conn)
        sendMsg(conn,msg)

def newBroadcast(msg):
    for name in clientsList:
        conn = usrnameToConn[name]
        sendMsg(conn,msg)

def waitingOrder():
    global clientsNum
    while True:
        order = input()
        if order == 'del':
            name = input('kick which usrname?')
            delusr(name)
        if order == 'clients':
            print(usrnameToConn)
            print(clientsList)
            print(clientsNum)
        if order == 'delall':
            tmplist = clientsList
            for name in tmplist:
                delusr(name)
            tmplist = []

# 等待用户发送消息,受到之后广播给大家
def waitingForMsg(conn,usrname):
    while usrname in clientsList:
        data = recvMsg(conn)
        if data == '#exit' : 
            delusr(usrname)
            newBroadcast(usrname + ' 退出聊天室 ')
            newBroadcast('#sub ' + usrname)
            break

        else : newBroadcast(usrname + ' : '+ data)
        if data != '' : print(usrname + ' : ' + data)
    
# 等待连接
def waitClientConnect():
    global clientsNum
    if clientsNum < 30:
        conn, addr = s.accept()     # 等待连接，阻塞式等待，等到了就执行后面的登录流程

        # 有人连接上了，就开启另一个等待连接线程
        threadWaiting = threading.Thread(target=waitClientConnect)
        threadWaiting.start()

        # 接收用户名和密码，并判断是否在已注册列表里
        usrname = recvMsg(conn)
        sendMsg(conn,'usrname received')
        passwrd = recvMsg(conn)
        sendMsg(conn,'passwrd received')
        recvMsg(conn)
        if usrname not in clientsList and usrname in usersList and usersList[usrname] == passwrd : 
            sendMsg(conn,'connect successfully')
            recvMsg(conn)
            print('connected by : ' + str(addr))
            clientsList.append(usrname)
            usrnameToConn[usrname] = conn
            clientsNum += 1

            # 把在线列表发给他
            sendMsg(conn, str(clientsNum))
            recvMsg(conn)
            for name in clientsList:
                sendMsg(conn, name)
                recvMsg(conn)
            
            # 告诉其他小伙伴有人上线了
            newBroadcast('欢迎 '+ usrname + ' 加入聊天室！')
            
            # 让其他在线人员更新列表
            for name in clientsList:
                if name == usrname : continue
                sendMsg(usrnameToConn[name],'#add ' + usrname)

            # 为用户开启等待消息线程
            threadNewReceiver = threading.Thread(target=waitingForMsg, args=(conn,usrname,))
            threadNewReceiver.start()

        else : sendMsg(conn,'connect refused')

threadWaiting = threading.Thread(target=waitClientConnect)
threadWaiting.start()

threadWaiting = threading.Thread(target=waitingOrder)
threadWaiting.start()