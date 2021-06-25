import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif',12))
        # 设置窗口控件提示消息
        self.setToolTip('今天是<b>星期五</b>')
        self.setWindowTitle('设置控件提示消息')
        self.setGeometry(300,300,200,300)
        # 添加Button
        self.button1 = QPushButton('应用')
        # 设置窗口控件提示消息
        self.button1.setToolTip('这是一个按钮')
        # 创建一个水平布局
        layout = QHBoxLayout()
        # 将按钮加在布局里
        layout.addWidget(self.button1)
        # 创建主框架
        mainFrame = QWidget()
        # 将水平布局放在框架上
        mainFrame.setLayout(layout)
        # 将框架充满整个窗口
        self.setCentralWidget(mainFrame)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())
