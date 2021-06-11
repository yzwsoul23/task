# -*- coding: utf-8 -*-
#使用utf-8字符编码
# Form implementation generated from reading ui file 'D:\zw_own\PyQt\Python3\testPyQt5_7\my_pyqt_book\layout_demo_LayoutManage.ui'
#读取ui文件'D:\texePyQt5\layoutWin.ui'生成窗口实现
# Created by: PyQt5 UI code generator 5.5.1
#由PyQt5 UI代码生成器5.15.4
# WARNING! All changes made in this file will be lost!
#警告:当pyuic5启动时，对该文件所做的任何手动更改将丢失
from PyQt5 import QtCore, QtGui, QtWidgets
#从PyQt5 引入QtCore, QtGui, QtWidgets类
class Ui_LayoutDemo(object):
#新建一个object的子类Ui_LayoutDemo
    def setupUi(self, LayoutDemo):
    #设一个setupUi函数
        LayoutDemo.setObjectName("LayoutDemo")
        #设置对象名字为LayoutDemo
        LayoutDemo.resize(565, 430)
        #调整对象LayoutDemo大小
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        #将对象尺寸策略长为Minimum，宽为Preferred
        #Minimum最小尺寸为规定尺寸，大可无穷
        #Preferred规定尺寸为默认尺寸，可调控
        sizePolicy.setHorizontalStretch(3)
        #设置水平拉伸为3
        sizePolicy.setVerticalStretch(6)
        #设置垂直拉伸为6
        sizePolicy.setHeightForWidth(LayoutDemo.sizePolicy().hasHeightForWidth())
        #设置LayoutDemo宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        LayoutDemo.setSizePolicy(sizePolicy)
        #设置LayoutDemo的尺寸策略为sizePolicy
        self.centralwidget = QtWidgets.QWidget(LayoutDemo)
        #将QtWidgets.QWidget的对象LayoutDemo赋值给self.centralwidget
        self.centralwidget.setObjectName("centralwidget")
        #设置self.centralwidget对象名字为centralwidget
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        #将QtWidgets.QWidget的对象self.centralwidget赋值给self.layoutWidget
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 504, 94))
        #设定elf.layoutWidget位置尺寸为QtCore.QRect的对象9, 9, 504, 94
        self.layoutWidget.setObjectName("layoutWidget")
        #设置self.layoutWidget对象名字为layoutWidget
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        #将QtWidgets.QHBoxLayout的对象self.layoutWidget赋值给self.horizontalLayout
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        #设置self.horizontalLayout尺寸约束为默认尺寸
        self.horizontalLayout.setObjectName("horizontalLayout")
        #设置self.horizontalLayout对象名字为horizontalLayout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        #将QtWidgets.QVBoxLayout的对象默认值赋值给self.verticalLayout
        self.verticalLayout.setObjectName("verticalLayout")
        #设置self.verticalLayout对象名字为verticalLayout
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        #将QtWidgets.QLabel的对象self.layoutWidget赋值给self.label_6
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        #设置self.label_6对象名字为label_6
        self.verticalLayout.addWidget(self.label_6)
        #将self.verticalLayout增加的小部件self.label_6
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        #将QtWidgets.QLabel的对象self.layoutWidget赋值给self.label_3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #将对象尺寸策略长为Preferred，宽为Preferred
        sizePolicy.setHorizontalStretch(0)
        #设置水平拉伸为0
        sizePolicy.setVerticalStretch(0)
        #设置垂直拉伸为0
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        #设置self.label_3宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        self.label_3.setSizePolicy(sizePolicy)
        #设置self.label_3的尺寸策略为sizePolicy
        self.label_3.setObjectName("label_3")
        #设置self.label_3对象名字为label_3
        self.verticalLayout.addWidget(self.label_3)
        #将self.verticalLayout增加的小部件self.label_3
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        #将QtWidgets.QLabel的对象self.layoutWidget赋值给self.label_4
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #将对象尺寸策略长为Preferred，宽为Preferred
        sizePolicy.setHorizontalStretch(0)
        #设置水平拉伸为0
        sizePolicy.setVerticalStretch(0)
        #设置垂直拉伸为0
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        #设置self.label_4宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        self.label_4.setSizePolicy(sizePolicy)
        #设置self.label_4的尺寸策略为sizePolicy
        self.label_4.setObjectName("label_4")
        #设置self.label_4对象名字为label_4
        self.verticalLayout.addWidget(self.label_4)
        #将self.verticalLayout增加的小部件self.label_4
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        #将QtWidgets.QLabel的对象self.layoutWidget赋值给self.label_5
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #将对象尺寸策略长为Preferred，宽为Preferred
        sizePolicy.setHorizontalStretch(0)
        #设置水平拉伸为0
        sizePolicy.setVerticalStretch(0)
        #设置垂直拉伸为0
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        #设置self.label_5宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        self.label_5.setSizePolicy(sizePolicy)
        #设置self.label_5的尺寸策略为sizePolicy
        self.label_5.setObjectName("label_5")
        #设置self.label_5对象名字为label_5
        self.verticalLayout.addWidget(self.label_5)
        #将self.verticalLayout增加的小部件self.label_5
        self.horizontalLayout.addLayout(self.verticalLayout)
        #将self.horizontalLayout增加垂直布局
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #将对象尺寸策略长为Minimum，宽为Expanding
        self.horizontalLayout.addItem(spacerItem)
        #将self.horizontalLayout增加间隔件
        self.gridLayout = QtWidgets.QGridLayout()
        #将QtWidgets.QGridLayout的默认对象赋值给self.gridLayout
        self.gridLayout.setObjectName("gridLayout")
        #设置self.gridLayout对象名字为gridLayout
        self.label = QtWidgets.QLabel(self.layoutWidget)
        #将QtWidgets.QLabel的对象self.layoutWidget赋值给self.label
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #将对象尺寸策略长为Preferred，宽为Preferred
        sizePolicy.setHorizontalStretch(0)
        #设置水平拉伸为0
        sizePolicy.setVerticalStretch(0)
        #设置垂直拉伸为0
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        #设置self.label宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        self.label.setSizePolicy(sizePolicy)
        #设置self.label的尺寸策略为sizePolicy
        self.label.setObjectName("label")
        #设置self.label对象名字为label
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        #elf.gridLayout增加部件self.labe及位置为0, 0, 1, 1
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        #将QtWidgets.QLabel的对象self.layoutWidget赋值给self.label_2
        self.label_2.setObjectName("label_2")
        #设置self.label_2对象名字为label_2
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        #elf.gridLayout增加部件self.labe_2及位置为0, 1, 1, 1
        self.doubleSpinBox_returns_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        #将QtWidgets.QDoubleSpinBox的对象self.layoutWidget赋值给self.doubleSpinBox_returns_min
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        #将对象尺寸策略长为Minimum，宽为Fixed
        sizePolicy.setHorizontalStretch(0)
        #设置水平拉伸为0
        sizePolicy.setVerticalStretch(1)
        #设置垂直拉伸为1
        sizePolicy.setHeightForWidth(self.doubleSpinBox_returns_min.sizePolicy().hasHeightForWidth())
        #设置self.doubleSpinBox_returns_min宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        self.doubleSpinBox_returns_min.setSizePolicy(sizePolicy)
        #设置self.doubleSpinBox_returns_min的尺寸策略为sizePolicy
        self.doubleSpinBox_returns_min.setMaximum(0.8)
        #设置self.doubleSpinBox_returns_min的尺寸最大为0.8
        self.doubleSpinBox_returns_min.setSingleStep(0.01)
        #设置self.doubleSpinBox_returns_min的单步为0.01
        self.doubleSpinBox_returns_min.setObjectName("doubleSpinBox_returns_min")
        #设置self.doubleSpinBox_returns_min对象名字为doubleSpinBox_returns_min
        self.gridLayout.addWidget(self.doubleSpinBox_returns_min, 1, 0, 1, 1)
        #elf.gridLayout增加部件self.doubleSpinBox_returns_min及位置为1, 0, 1, 1
        self.doubleSpinBox_returns_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        #将QtWidgets.QDoubleSpinBox的对象self.layoutWidget赋值给self.doubleSpinBox_returns_max
        self.doubleSpinBox_returns_max.setObjectName("doubleSpinBox_returns_max")
        #设置self.doubleSpinBox_returns_max对象名字为doubleSpinBox_returns_max
        self.gridLayout.addWidget(self.doubleSpinBox_returns_max, 1, 1, 1, 1)
        #elf.gridLayout增加部件self.doubleSpinBox_returns_max及位置为1, 1, 1, 1
        self.doubleSpinBox_maxdrawdown_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        #将QtWidgets.QDoubleSpinBox的对象self.layoutWidget赋值给self.doubleSpinBox_maxdrawdown_min
        self.doubleSpinBox_maxdrawdown_min.setObjectName("doubleSpinBox_maxdrawdown_min")
        #设置self.doubleSpinBox_maxdrawdown_min对象名字为doubleSpinBox_maxdrawdown_min
        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_min, 2, 0, 1, 1)
        #elf.gridLayout增加部件self.doubleSpinBox_maxdrawdown_min及位置为2, 0, 1, 1
        self.doubleSpinBox_maxdrawdown_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        #将QtWidgets.QDoubleSpinBox的对象self.layoutWidget赋值给self.doubleSpinBox_maxdrawdown_max
        self.doubleSpinBox_maxdrawdown_max.setObjectName("doubleSpinBox_maxdrawdown_max")
        #设置self.doubleSpinBox_maxdrawdown_maxt对象名字为doubleSpinBox_maxdrawdown_max
        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_max, 2, 1, 1, 1)
        #elf.gridLayout增加部件self.doubleSpinBox_maxdrawdown_max及位置为2, 1, 1, 1
        self.doubleSpinBox_sharp_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        #将QtWidgets.QDoubleSpinBox的对象self.layoutWidget赋值给self.doubleSpinBox_sharp_min
        self.doubleSpinBox_sharp_min.setObjectName("doubleSpinBox_sharp_min")
        #设置self.doubleSpinBox_sharp_min对象名字为doubleSpinBox_sharp_min
        self.gridLayout.addWidget(self.doubleSpinBox_sharp_min, 3, 0, 1, 1)
        #elf.gridLayout增加部件self.doubleSpinBox_sharp_min及位置为3, 0, 1, 1
        self.doubleSpinBox_sharp_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        #将QtWidgets.QDoubleSpinBox的对象self.layoutWidget赋值给self.doubleSpinBox_sharp_max
        self.doubleSpinBox_sharp_max.setObjectName("doubleSpinBox_sharp_max")
        #设置self.doubleSpinBox_sharp_max对象名字为doubleSpinBox_sharp_max
        self.gridLayout.addWidget(self.doubleSpinBox_sharp_max, 3, 1, 1, 1)
        #elf.gridLayout增加部件self.doubleSpinBox_sharp_max及位置为3, 1, 1, 1
        self.horizontalLayout.addLayout(self.gridLayout)
        #将self.horizontalLayout增加网格布局
        self.line = QtWidgets.QFrame(self.layoutWidget)
        #将QtWidgets.QFrame的对象self.layoutWidget赋值给self.line
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        #设置self.line的框架形状为VLine
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        #设置self.line的帧阴影为Sunken
        self.line.setObjectName("line")
        #设置self.line对象名字为line
        self.horizontalLayout.addWidget(self.line)
        #将self.verticalLayout增加的小部件self.line
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        #将对象尺寸策略长为Preferred，宽为Minimum
        self.horizontalLayout.addItem(spacerItem1)
        #将self.horizontalLayout增加间隔件
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        #将QtWidgets.QPushButton的对象self.layoutWidget赋值给pushButton
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        #将对象尺寸策略长为Fixed，宽为Maximum
        sizePolicy.setHorizontalStretch(0)
        #设置水平拉伸为0
        sizePolicy.setVerticalStretch(0)
        #设置垂直拉伸为0
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        #设置self.pushButton宽度的高度为sizePolicy().hasHeightForWidth()的默认值
        self.pushButton.setSizePolicy(sizePolicy)
        #设置self.pushButton的尺寸策略为sizePolicy
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        #设置self.pushButton的尺寸为0，0
        self.pushButton.setObjectName("pushButton")
        #设置self.pushButton对象名字为pushButton
        self.horizontalLayout.addWidget(self.pushButton)
        #将self.verticalLayout增加的小部件self.pushButton
        LayoutDemo.setCentralWidget(self.centralwidget)
        #设置LayoutDemo中心部件为self.centralwidget
        self.menubar = QtWidgets.QMenuBar(LayoutDemo)
        #将QtWidgets.QMenuBar的对象LayoutDemo赋值给self.menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 23))
        #设定elf.menubar位置尺寸为QtCore.QRect的对象0, 0, 565, 23
        self.menubar.setObjectName("menubar")
        #设置self.menubar对象名字为menubar
        LayoutDemo.setMenuBar(self.menubar)
        #设置LayoutDemo菜单栏为self.menubar
        self.statusbar = QtWidgets.QStatusBar(LayoutDemo)
        #将QtWidgets.QStatusBar的对象LayoutDemo赋值给self.statusbar
        self.statusbar.setObjectName("statusbar")
        #设置self.statusbar对象名字为statusbar
        LayoutDemo.setStatusBar(self.statusbar)
        #设置LayoutDemo的状态栏为self.statusbar
        self.label_5.setBuddy(self.doubleSpinBox_sharp_min)
        #将self.label_5和self.doubleSpinBox_sharp_min设置连接

        self.retranslateUi(LayoutDemo)
        #重传用户界面LayoutDemo
        QtCore.QMetaObject.connectSlotsByName(LayoutDemo)
        #将LayoutDemo内元素，按名称连接

    def retranslateUi(self, LayoutDemo):
    #设定retranslateUi函数
        _translate = QtCore.QCoreApplication.translate
         #将QtCore.QCoreApplication.translate的对象stranslate赋值给_translate
        LayoutDemo.setWindowTitle(_translate("LayoutDemo", "MainWindow"))
        #将窗口标题设为MainWindow
        self.label_3.setText(_translate("LayoutDemo", "收益"))
        #将self.label_3显示名称设为收益
        self.label_4.setText(_translate("LayoutDemo", "最大回撤"))
        #将self.label_4显示名称设为最大回撤
        self.label_5.setText(_translate("LayoutDemo", "&sharp比"))
        #将self.label_5显示名称设为&sharp比
        self.label.setText(_translate("LayoutDemo", "最小值"))
        #将self.label显示名称设为最小值
        self.label_2.setText(_translate("LayoutDemo", "最大值"))
        #将self.label_2显示名称设为最大值
        self.pushButton.setText(_translate("LayoutDemo", "开始"))
        #将self.pushButton显示名称设为开始


if __name__ == "__main__":
#判断是否运行程序
    import sys
    #引入sys模块
    app = QtWidgets.QApplication(sys.argv)
    #设置程序打开地址
    LayoutDemo = QtWidgets.QMainWindow()
    #将QtWidgets.QMainWindow的默认对象赋值给LayoutDemo
    ui = Ui_LayoutDemo()
    #设置用户接口为LayoutDemo类的默认对象
    ui.setupUi(LayoutDemo)
    #ui设置用户接口为LayoutDemo
    LayoutDemo.show()
    #显示窗口LayoutDemo
    sys.exit(app.exec_())
    #循环app的主程序直到不再调用.exit

