# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_clientLogin(object):
    def setupUi(self, clientLogin):
        clientLogin.setObjectName("clientLogin")
        clientLogin.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(clientLogin.sizePolicy().hasHeightForWidth())
        clientLogin.setSizePolicy(sizePolicy)
        clientLogin.setMinimumSize(QtCore.QSize(400, 300))
        clientLogin.setMaximumSize(QtCore.QSize(400, 300))
        self.centralWidget = QtWidgets.QWidget(clientLogin)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 80, 301, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(11, 11, 0, 11)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.usrnameEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.usrnameEdit.setObjectName("usrnameEdit")
        self.horizontalLayout.addWidget(self.usrnameEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passwrdEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.passwrdEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.passwrdEdit.setMaxLength(16)
        self.passwrdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwrdEdit.setObjectName("passwrdEdit")
        self.horizontalLayout_2.addWidget(self.passwrdEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnLogin = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogin.setGeometry(QtCore.QRect(130, 210, 93, 28))
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegister = QtWidgets.QPushButton(self.centralWidget)
        self.btnRegister.setGeometry(QtCore.QRect(250, 210, 93, 28))
        self.btnRegister.setObjectName("btnRegister")
        clientLogin.setCentralWidget(self.centralWidget)

        self.retranslateUi(clientLogin)
        QtCore.QMetaObject.connectSlotsByName(clientLogin)

    def retranslateUi(self, clientLogin):
        _translate = QtCore.QCoreApplication.translate
        clientLogin.setWindowTitle(_translate("clientLogin", "登录"))
        self.label.setText(_translate("clientLogin", "用户名"))
        self.label_2.setText(_translate("clientLogin", "密码"))
        self.btnLogin.setText(_translate("clientLogin", "登录"))
        self.btnLogin.setShortcut(_translate("clientLogin", "Return"))
        self.btnRegister.setText(_translate("clientLogin", "注册"))