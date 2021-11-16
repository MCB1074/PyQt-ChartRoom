from PyQt5.QtWidgets import *
from clientChatRoom import *
from clientLogin import *
from socket import *
import sys
import threading

# 自定义收发消息函数
def recvMsg(client):
    msg = client.recv(1024).decode('utf-8')
    if msg != '':
        print('Server : ' + msg)
    return msg

def sendMsg(client,msg):
    client.send(msg.encode('utf-8'))
    print('Client : ' + msg)


# 第一种调用方法
class loginWindow(QMainWindow, Ui_clientLogin):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 按键关联
        self.btnLogin.clicked.connect(self.login)

    #自定义函数
    def login(self):
        config = open("serverConfig.txt")

        ip = config.readline()
        port = int(config.readline())

        config.close()

        # 初始化socket
        global myConn
        myConn = socket(AF_INET,SOCK_STREAM)
        myConn.connect((ip,port))

        usrname = self.usrnameEdit.text()
        sendMsg(myConn,usrname)
        recvMsg(myConn)
        sendMsg(myConn,self.passwrdEdit.text())
        recvMsg(myConn)
        sendMsg(myConn,'done')
        if(recvMsg(myConn) == 'connect successfully'):
            sendMsg(myConn, usrname + ' connected')
            self.ui_CharRoom = charRoomWindow()

            # 初始化聊天室
            self.nameDict = {}
            clientsNum = int(recvMsg(myConn))
            sendMsg(myConn, 'num received')
            for i in range(clientsNum):
                name = recvMsg(myConn)
                self.nameDict[name] = i
                sendMsg(myConn, 'name received')
                self.ui_CharRoom.connectClientsList.addItem(name)
            # print(self.nameDict)
            self.recvMsgOnce()

            self.ui_CharRoom.btnSendMsg.clicked.connect(self.sayToAll)
            self.ui_CharRoom.show()

            waitMsgThread = threading.Thread(target=self.waitMsg)
            waitMsgThread.start()

            self.close()

    def recvMsgOnce(self):
        msg = myConn.recv(1024).decode('utf-8')
        self.ui_CharRoom.msgRecorder.append(msg)

    def waitMsg(self):
        while True:
            msg = myConn.recv(1024).decode('utf-8')
            if msg[0] == '#':
                if msg[1:4] == 'add':
                    name = msg[5:]
                    self.ui_CharRoom.connectClientsList.addItem(name)
                    self.nameDict[name] = len(self.nameDict)
                if msg[1:4] == 'sub':
                    name = msg[5:]
                    self.ui_CharRoom.connectClientsList.takeItem(self.nameDict[name])
                    del self.nameDict[name]

                if msg[1:5] == 'exit' : self.ui_CharRoom.close()
                continue
            self.ui_CharRoom.msgRecorder.append(msg)

    def sayToAll(self):
        msg = self.ui_CharRoom.sendMsgEdit.toPlainText()
        sendMsg(myConn, msg)
        self.ui_CharRoom.sendMsgEdit.clear()
        if(msg == '#exit') : self.ui_CharRoom.close()


class charRoomWindow(QMainWindow, Ui_clientChatRoom):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnQuitClient.clicked.connect(self.close)

    def closeEvent(self,event):
        result = QMessageBox.question(self,
                      "确认退出",
                      "确认退出程序吗 ？",
                      QMessageBox.Yes| QMessageBox.No)
        if result == QMessageBox.Yes:
            sendMsg(myConn,'#exit')
            event.accept()
        else : event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ui_login = loginWindow()
    ui_login.show()

    sys.exit(app.exec_())

# # 第二种调用方法
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainwindow = QMainWindow()

#     ui_login = Ui_clientLogin()
#     ui_chatRoom = Ui_clientChatRoom()

#     ui_login.setupUi(mainwindow)
#     mainwindow.show()
#     sys.exit(app.exec_())
