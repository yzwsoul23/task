import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self,parent=None):
        super(IconForm,self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,250)
        #设置主窗口标题
        self.setWindowTitle('设置窗口图标')

        #设置窗口图标
        self.setWindowIcon(QIcon('./images/Basilisk.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #设置应用程序图标
    # app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())