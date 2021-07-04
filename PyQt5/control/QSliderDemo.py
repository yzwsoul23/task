'''

滑块控件（QSlider）

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,700)

        layout = QVBoxLayout()
        self.label = QLabel('你好 PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)
        # 添加水平方向的滑块控件
        self.slider = QSlider(Qt.Horizontal)



        # 设置最小值
        self.slider.setMinimum(12)
        # 设置最大值
        self.slider.setMaximum(48)

        # 步长
        self.slider.setSingleStep(1)

        # 设置当前值
        self.slider.setValue(18)

        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBothSides)
        # 设置刻度的间隔
        self.slider.setTickInterval(1)

        layout.addWidget(self.slider)
        # 连接值被更改信号和valueChange槽函数
        self.slider.valueChanged.connect(self.valueChange)
        # 添加垂直方向的滑块控件
        self.slider1 = QSlider(Qt.Vertical)
        layout.addWidget(self.slider1)
        # 设置最小值
        self.slider1.setMinimum(10)
        # 设置最大值
        self.slider1.setMaximum(60)

        # 步长
        self.slider1.setSingleStep(1)

        # 设置当前值
        self.slider1.setValue(30)

        # 设置刻度的位置，刻度在下方
        self.slider1.setTickPosition(QSlider.TicksLeft)
        # 设置刻度的间隔
        self.slider1.setTickInterval(2)
        # 连接值被更改信号和valueChange槽函数
        self.slider1.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        # 输出信号的值
        print('当前值：%s' % self.sender().value())
        # 将size设为信号的值
        size = self.sender().value() * 4
        # 设置标签文本的字号为size
        self.label.setFont(QFont('Arial',size))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())