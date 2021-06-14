import sys
#引用sys模块
from PyQt5.QtWidgets import QApplication, QMainWindow
#从PyQt5.QtWidgets引用QApplication, QMainWindow类
from MainWinSignalSlog01 import Ui_Form
#从MainWinSignalSlog01引用Ui_Form类

class MyMainWindow(QMainWindow, Ui_Form):
#设置QMainWindow, Ui_Form的子类MyMainWindow
    def __init__(self, parent=None):
    #设定初始值函数
        super(MyMainWindow, self).__init__(parent)
        #引用父类函数__init__对象parent
        self.setupUi(self)
        #使用Ui_Form类里setupUi函数



if __name__ == "__main__":
#判断是否运行
    app = QApplication(sys.argv)
    #设置路径
    myWin = MyMainWindow()
    myWin.show()
    #显示MyMainWindow()类
    sys.exit(app.exec_())
    #运行主循环直到exit()被调用退出时返回状态代码进入程序的主循环