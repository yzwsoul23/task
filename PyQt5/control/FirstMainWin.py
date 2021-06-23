import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        #设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        #设置主窗口尺寸
        self.resize(400,300)
        #设置状态栏
        self.status =self.statusBar()
        #状态栏展示消息
        self.status.showMessage('只存在五秒的消息',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #设置应用程序图标
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())