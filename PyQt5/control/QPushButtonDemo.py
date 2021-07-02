'''

按钮控件（QPushButton）

QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox


'''


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QPushButtonDemo(QDialog) :
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button1')
        # 设置按钮为选中状态
        self.button1.setCheckable(True)
        # 切换可检查按钮的状态
        self.button1.toggle()
        # 将按钮被单击连接按钮判断是否被选中并输出的槽函数
        self.button1.clicked.connect(self.buttonState)
        # 将按钮被单击连接显示按钮1被点击的槽函数
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))

        layout.addWidget(self.button1)

        # 在文本前面显示图像

        self.button2 = QPushButton('图像按钮')
        # 设置图标
        self.button2.setIcon(QIcon(QPixmap('./images/python.png')))
        # 将按钮被单击连接按钮判断是否被选中并输出的槽函数
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用的按钮')
        # 按钮设置为不可用
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        # 设置按钮热键
        self.button4 = QPushButton('&MyButton')
        # 设置默认按钮
        self.button4.setDefault(True)
        # 将按钮被单击连接按钮判断是否被选中并输出的槽函数
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def buttonState(self):
        # 检查按钮是否被选中并分别处理
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
