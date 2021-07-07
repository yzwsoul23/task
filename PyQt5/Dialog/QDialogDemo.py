'''

对话框：QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

QMainWindow
QWidget
QDialog

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        # 连接按钮点击信号和显示对话框槽函数
        self.button.clicked.connect(self.showDialog)

    # 定义显示对话框槽函数
    def showDialog(self):
        # 创建对话框
        dialog = QDialog()
        # 创建按钮放入对话框
        button = QPushButton('确定',dialog)
        # 连接按钮点击信号和关闭对话框槽函数
        button.clicked.connect(dialog.close)
        button.move(20,20)
        dialog.setWindowTitle('对话框')
        # 设置窗口显示模式不关掉对话框主窗口就无法操作
        dialog.setWindowModality(Qt.ApplicationModal)
        # 显示对话框
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())

