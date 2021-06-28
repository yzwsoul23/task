'''

QLineEdit综合案例

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        # 创建整式输入框
        edit1 = QLineEdit()
        # 使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  # 设置最大长度不超过9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,3))

        edit3 = QLineEdit()
        edit3.setInputMask('1999%9_999999;我')

        edit4 = QLineEdit()
        # 将文本更改连接.textChanged方法
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        # 输入隐藏显示给用户
        edit5.setEchoMode(QLineEdit.Password)
        # 将输入完成信号连接.enterPress方法
        edit5.editingFinished.connect(self.enterPress)

        # 设置输入框文本
        edit6 = QLineEdit('Hello PyQt5')
        # 将输入框设置为只读
        edit6.setReadOnly(True)

        # 设置窗体布局
        formLayout = QFormLayout()
        # 将文本和输入框以一行行的形式去添加在窗体
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验',edit2)
        formLayout.addRow('Input Mask',edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('密码',edit5)
        formLayout.addRow('只读',edit6)
        # 将窗体添加窗口
        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit综合案例')
    def textChanged(self,text):
        print('输入的内容：' + text)

    def enterPress(self):
        print('已输入值')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())