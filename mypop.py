# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mypop.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(285, 165)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.plainTextEdit_info = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_info.setObjectName("plainTextEdit_info")
        self.verticalLayout.addWidget(self.plainTextEdit_info)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.verticalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.verticalLayout.addWidget(self.pushButton_cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "请输入你的信息"))
        self.pushButton_ok.setText(_translate("Dialog", "ok"))
        self.pushButton_cancel.setText(_translate("Dialog", "cancel"))
