# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignalSlog01.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#引用QtCore, QtGui, QtWidgets类

class Ui_Form(object):
#设置object的子类Ui_Form
    def setupUi(self, Form):
    #设置setupUi函数
        Form.setObjectName("Form")
        #设置Form名称为Form
        Form.resize(452, 296)
        #设置Form大小为Form452, 296
        self.closeWinBtn = QtWidgets.QPushButton(Form)
        #设置closeWinBtn为QtWidgets.QPushButton(Form)
        self.closeWinBtn.setGeometry(QtCore.QRect(150, 80, 121, 31))
        #设置self.closeWinBtn位置大小为150, 80, 121, 31
        self.closeWinBtn.setObjectName("closeWinBtn")
        #设置closeWinBtn名称为closeWinBtn

        self.retranslateUi(Form)
        #重传用户界面Form
        self.closeWinBtn.clicked.connect(Form.close)
        #l连接关闭窗口信号
        QtCore.QMetaObject.connectSlotsByName(Form)
        #按Form名称连接插槽

    def retranslateUi(self, Form):
    #设置retranslateUi函数
        _translate = QtCore.QCoreApplication.translate
        #创建QCoreApplication对象_translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #设置窗口名称Form
        self.closeWinBtn.setText(_translate("Form", "关闭窗口"))
        #设置closeWinBtn按钮显示名称关闭窗口

