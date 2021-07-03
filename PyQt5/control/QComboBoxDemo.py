'''

下拉列表控件（QComboBox）

1. 如果将列表项添加到QComboBox控件中

2. 如何获取选中的列表项

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择编程语言')

        self.cb = QComboBox()
        # 创建项目
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Ruby'])
        # 连接索引变化信号和selectionChange槽函数
        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self,i):
        # 将标签设置为当前选中文本
        self.label.setText(self.cb.currentText())
        # 设置标签大小
        self.label.adjustSize()
        # 输出列表各索引及对应的项
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        # 输出当前索引及对应的项
        print('current index',i,'selection changed', self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())