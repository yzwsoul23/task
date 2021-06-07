# -*- coding: utf-8 -*-  #告诉编辑器下面的代码是utf-8编码的，(- *-）是让编辑器区分注释的符号

import sys #引入sys模块 sys模块是用来处理python运行时环境的,封装了系统的信息和接口
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
#从PyQt5模块的QtWidgets父类中引用QPushButton, QWidget, QApplication子类
#PyQt是对Qt里的类进行Pyton化的封装
#QtWidgets类是对界面元素的设定
#QPushButton类是对按钮的设定
#QWidget类是对窗口小部件的设定
#QApplication类是对图形界面整体的设定
class WinForm (QWidget):
    #设定一个QWidget的子类WinForm
    def __init__(self, parent=None):
        #初始化属性并将窗口属性默认值设为主窗口
        super(WinForm, self).__init__(parent)
        #从WinForm父类QWidget继承属性parent
        self.setGeometry(300, 300, 350, 350)
        #设置窗口位置尺寸setGeometry(x轴，y轴，宽，高)
        #.setGeometry是QWidget的函数
        self. setWindowTitle("点击按钮关闭窗口")
        #设置窗口标题 点击按钮关闭窗口
        #.setWindowTitle是QMessageBox的函数(QMessageBox是QWidget的子类)
        #引用了父类如果子类改写了父类的属性和方法可以调用
        #引用了父类如果子类有父类没有的属性和方法不能调用
        quit=QPushButton("Close", self)
        #设定一个按钮quit并名字属性为Close
        quit.setGeometry(10, 10, 60, 35)
        #设定按钮quit位置尺寸
        quit.setStyleSheet("background-color: red")
        #设定按钮quit样式背景为红色
        #.setStyleSheet是QApplication的函数
        quit.clicked.connect(self.close)
        #通过按钮关闭事件
        #quit.clicked是按钮发出的信号
        #.connect是连接两者之间关系
        #self.close是关闭该按钮所在的窗口
if __name__=="__main__":
#判断当前运行的是否为自己的模块
#if__name__=="__main__":判断模块是不是被引用
#如果是自己运行__name__==__main__成立其中的代码就运行
#如果是被引用__name__==模块名,成立其中的代码就不运行
     app=QApplication(sys.argv)#将本文件定义为应用app
     #app=QApplication定义应用对象
     #sys.argv本身文件的路径
     win=WinForm()
     #设定WinForm对象win
     win.show()
     #显示窗口win
     #.show函数是QWindow的(QWindow是QtGui的子类)
     sys.exit(app.exec_())#循环app的主程序直到不再调用.exit
     #sys.exit(n)退出应用程序
     #app.exec_()循环app的主程序
