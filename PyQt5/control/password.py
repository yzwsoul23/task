from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class PassWord(QWidget):
    def __init__(self):
        super(PassWord, self).__init__()
        self.initUI()

    def initUI(self):
        self.edit = QLineEdit()
        self.edit.setPlaceholderText('请输入密码')
        self.edit.setEchoMode(QLineEdit.Password)
        self.edit.setMinimumSize(200,20)
        self.edit.returnPressed.connect(self.txt)
        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')  # 正则表达式
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.edit.setValidator(validator)
        self.edit.setClearButtonEnabled(True)

        self.button = QPushButton('θ')
        self.button.setToolTip('显示密码')
        self.button.setMaximumSize(25,25)
        self.button.pressed.connect(self.buttonState)
        self.button.released.connect(self.buttonrelease)

        hboxlayou = QHBoxLayout()
        hboxlayou.addWidget(self.edit)
        hboxlayou.addWidget(self.button)
        self.setLayout(hboxlayou)
        self.setWindowTitle('输入密码')

    def buttonState(self):
        self.edit.setEchoMode(QLineEdit.Normal)

    def buttonrelease(self):
        self.edit.setEchoMode(QLineEdit.Password)

    def txt(self):
        if self.edit.text == '2019520474':
            dialog = QDialog()
            dialog.resize(50,50)
            button = QPushButton('密码正确',dialog)
            button.move(25, 25)
            dialog.setWindowTitle('密码正确✔')
            # 设置窗口显示模式不关掉对话框主窗口就无法操作
            dialog.setWindowModality(Qt.ApplicationModal)
            # 显示对话框
            dialog.exec()
        else:
            dialog = QDialog()
            dialog.resize(50, 75)
            button = QPushButton('重新输入', dialog)
            button.move(23,25)
            button.clicked.connect(self.edit.clear)
            button.clicked.connect(dialog.close)
            dialog.setWindowTitle('密码错误✘')
            # 设置窗口显示模式不关掉对话框主窗口就无法操作
            dialog.setWindowModality(Qt.ApplicationModal)
            # 显示对话框
            dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PassWord()
    main.show()
    sys.exit(app.exec_())
