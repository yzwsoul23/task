# -*- coding: utf-8 -*-
#utf-8字符编码

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_MainWinSignalSlog04 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkBox.setChecked(True)
        #设置默认选择为被选中
    
    @pyqtSlot(bool)
    def on_checkBox_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.label.setVisible(checked)
        self.lineEdit.setEnabled(checked)

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myWin=MainWindow()
    myWin.show()
    sys.exit(app.exec_())
