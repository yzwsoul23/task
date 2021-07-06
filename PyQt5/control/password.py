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
        self.edit.textEdited.connect(self.txt)
        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')  # 正则表达式
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.edit.setValidator(validator)
        self.edit.setClearButtonEnabled(True)

        self.button = QPushButton('显示')
        self.button.setCheckable(True)
        self.button.setMaximumSize(40,25)
        self.button.toggle()
        self.button.clicked.connect(self.buttonState)

        hboxlayou = QHBoxLayout()
        hboxlayou.addWidget(self.edit)
        hboxlayou.addWidget(self.button)
        self.setLayout(hboxlayou)
        self.setWindowTitle('输入密码')

    def buttonState(self):
        if self.button.isChecked():
            self.edit.setEchoMode(QLineEdit.Normal)
        else:
            self.edit.setEchoMode(QLineEdit.Password)

    def txt(self, text):
        if text == '2019520474':
            self.setWindowTitle('密码正确')
        else:
            self.setWindowTitle('密码错误')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PassWord()
    main.show()
    sys.exit(app.exec_())
