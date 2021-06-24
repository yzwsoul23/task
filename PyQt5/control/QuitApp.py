import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp,self).__init__()
        self.resize(300,200)
        self.setWindowTitle('退出应用程序')

        # 添加Button
        self.button1 = QPushButton('退出应用')
        # 将信号与槽绑定
        self.button1.clicked.connect(self.onClick_Button)
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


    # 按钮单击事件方法(自定义的槽)
    def onClick_Button(self):
        # sender函数获得发送消息的对象
        sender = self.sender()
        # 输出Button的文本
        print(sender.text()+'按钮被按下')
        # 获取QApplication单例对象
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApp()
    main.show()

    sys.exit(app.exec_())
