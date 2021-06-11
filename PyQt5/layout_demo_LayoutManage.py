# -*- coding: utf-8 -*-
#以下代码使用utf-8字符编码
"""
Module implementing LayoutDemo. 
"""
#以下代码实现LayoutDemo模块
from PyQt5.QtCore import pyqtSlot
#从 PyQt5.QtCore类 导入 pyqtSlot
#pyqtSlot是槽，和信号实现对象之间的通讯
from PyQt5.QtWidgets import QMainWindow, QApplication
#从 PyQt5.QtWidgets类 导入 QMainWindow, QApplication类
#QMainWindow类提供一个主应用程序窗口
#QApplication类管理GUI应用程序的控制流和主要设置
from Ui_layout_demo_LayoutManage import Ui_LayoutDemo
#从 Ui_layout_demo_LayoutManage文件 导入 Ui_LayoutDemo类

class LayoutDemo(QMainWindow, Ui_LayoutDemo):
#创建QMainWindow和Ui_LayoutDemo的子类LayoutDemo
    """
    Class documentation goes here.
    """
    #声明类的文档再此
    def __init__(self, parent=None):
    #创建初始属性
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LayoutDemo, self).__init__(parent)
        #用来调用LayoutDemo父类方法__init__(parent)
        self.setupUi(self)
        #使用setupUi函数
    
    @pyqtSlot()
    #定义指定信号槽对应的处理方法
    def on_pushButton_clicked(self):
    #定义函数on_pushButton_clicked
        """
        Slot documentation goes here.
        """
        #槽位文档在此
        print('收益_min:',self.doubleSpinBox_returns_min.text())
        print('收益_max:',self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:',self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:',self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:',self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:',self.doubleSpinBox_sharp_max.text())
        #打印对象对应文本


if __name__ == "__main__":
#判断是否运行程序
    import sys
    #引用sys模块

    app = QApplication(sys.argv)
    #设置程序打开地址
    ui = LayoutDemo()
    #设置用户接口为LayoutDemo类的默认对象
    ui.show()
    #显示ui元素
    sys.exit(app.exec_())
    #循环app的主程序直到不再调用.exit
