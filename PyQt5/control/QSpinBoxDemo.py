'''

计数器控件（QSpinBox）


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSpinBox演示')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        # 设置对齐模式
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb = QSpinBox()
        # 设置初始值
        self.sb.setValue(5)
        # 设置计数器范围
        self.sb.setRange(-10,101)
        # 设置单次调整步数(步进值)
        self.sb.setSingleStep(5)
        layout.addWidget(self.sb)
        # 设置计数器前缀
        self.sb.setPrefix('数值: ')
        # 最小值
        self.sb.setMinimum(-2)
        # 最大值
        self.sb.setMaximum(80)
        # 连接值被更改信号和valueChange槽函数
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        # 将标签文本设置为计数器的值
        self.label.setText('当前值：' + str(self.sb.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())