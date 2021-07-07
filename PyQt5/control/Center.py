# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
#QtWidgets不包含QFont必须调用QtGui

class MessageBox(QtWidgets.QWidget):
#继承自父类QtWidgets.QWidget
    def __init__(self):
        #parent = None代表此QWidget属于最上层的窗口,也就是MainWindows.
        QtWidgets.QWidget.__init__(self)
        #因为继承关系，要对父类初始化
        #通过super初始化父类，__init__()函数无self，若直接QtWidgets.QWidget.__init__(self)，括号里是有self的
        self.setGeometry(300, 300, 600,400)
        # setGeometry()方法完成两个功能--设置窗口在屏幕上的位置和设置窗口本身的大小。它的前两个参数是窗口在屏幕上的x和y坐标。后两个参数是窗口本身的宽和高
        #self.resize(1000, 500)  # 设置窗体大小，本行可有可无。
        self.center()#自定义一个居中的函数
        self.setWindowTitle('弹窗居中窗口')  # 仅仅设置窗体标题，不设置位置。
        self.setToolTip(u'<b>程序</b>提示')#调用setToolTip()方法,该方法接受富文本格式的参数,css之类。
        QtWidgets.QToolTip.setFont(QFont('华文楷体', 10))#设置字体以及字体大小
        #当我们关闭一个窗口时，在PyQt中就会触发一个QCloseEvent的事件，正常情况下会直接关闭这个窗口，
        #但是我们不希望这样的事情发生，所以我们需要重新定义QCloseEvent，函数名称为closeEvent不可变
    def closeEvent(self,event):#函数名固定不可变
        reply=QtWidgets.QMessageBox.question(self,u'警告',u'确认退出?',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        #QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply==QtWidgets.QMessageBox.Yes:
            event.accept()#关闭窗口
        else:
            event.ignore()#忽视点击X事件
    def center(self):
        screen=QtWidgets.QDesktopWidget().screenGeometry()#获取屏幕分辨率
        #QtWidgets.QDesktopWidget().screenGeometry()中QDesktopWidget()也有括号
        size=self.geometry()#获取窗口尺寸
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)#利用move函数窗口居中
app=QtWidgets.QApplication(sys.argv)
window=MessageBox()
window.show()
sys.exit(app.exec_())