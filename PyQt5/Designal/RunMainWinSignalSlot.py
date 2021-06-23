#导入相关模块
import sys
import MainWinSignalSlot
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个主窗口
    mainwindow = QMainWindow()
    # 调用ui文件里的类
    ui = MainWinSignalSlot.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())