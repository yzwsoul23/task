import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

def onClick_Button():
    print('第一种:坐标算标题栏的(窗口),尺寸算工作区的')
    print('widget.x() = %d' % widget.x())
    print('widget.y() = %d' % widget.y())
    print('widget.width() = %d' % widget.width())
    print('widget.height() = %d' % widget.height())

    print('第二种:坐标不算标题栏(工作区),尺寸算工作区的')
    print('widget.geometry().x() = %d' % widget.geometry().x())
    print('widget.geometry().y() = %d' % widget.geometry().y())
    print('widget.geometry().width() = %d' % widget.geometry().width())
    print('widget.geometry().height() = %d' % widget.geometry().height())

    print('第三种:坐标算标题栏的,尺寸算窗口的')
    print('widget.frameGeometry().x() = %d' % widget.frameGeometry().x())
    print('widget.frameGeometry().y() = %d' % widget.frameGeometry().y())
    print('widget.frameGeometry().width() = %d' % widget.frameGeometry().width())
    print('widget.frameGeometry().height() = %d' % widget.frameGeometry().height())

app = QApplication(sys.argv)
# 创建窗口
widget = QWidget()
# 将按钮放置在窗口上
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)

btn.move(24,52)
widget.resize(300,240) #设置工作区的宽高
widget.move(250,300)
widget.setWindowTitle('屏幕坐标')
widget.show()

sys.exit(app.exec_())