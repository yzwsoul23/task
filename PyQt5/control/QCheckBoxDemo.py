'''

复选框控件（QCheckBox）

3种状态

未选中：0

半选中：1

选中：2

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')

        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        # 连接复选框状态改变信号和将复选框参数传给checkboxState的lanbda的槽函数
        self.checkBox1.stateChanged.connect(lambda:self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox('复选框控件2')
        # 连接复选框状态改变信号和将复选框参数传给checkboxState的lanbda的槽函数
        self.checkBox2.stateChanged.connect(lambda:self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox('半选中')
        # 连接复选框状态改变信号和将复选框参数传给checkboxState的lanbda的槽函数
        self.checkBox3.stateChanged.connect(lambda:self.checkboxState(self.checkBox3))
        # 将复选框设为三种状态
        self.checkBox3.setTristate(True)
        # 检查状态设为部分检查
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def checkboxState(self,cb):
        # 监测各复选框状态并输出
        check1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + ',checkState=' + str(self.checkBox1.checkState()) + '\n'
        check2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())