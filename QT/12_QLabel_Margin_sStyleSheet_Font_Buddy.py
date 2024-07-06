import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class QLabelStyleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.showWindow()

    def initWindow(self):
        self.label1 = QLabel("Left Margin10",self)
        self.label1.move(10,110)
        self.label1.resize(90,90)
        self.label1.setStyleSheet("border: 1px solid black")
        self.label1.setAlignment(Qt.AlignLeft)
        self.label1.setMargin(10) # 마진 설정

        self.label2 = QLabel("Left",self)
        self.label2.move(10, 210)
        self.label2.resize(90,90)
        self.label2.setStyleSheet("border: 3px dashed red")
        self.label2.setAlignment(Qt.AlignLeft)

        self.label3 = QLabel("Center",self)
        self.label3.move(110, 10)
        self.label3.resize(90,90)
        self.label3.setStyleSheet("border: solid; border-color:red blue green yellow; border-width: 1px 2px 3px 4px") # width : 탑 오른쪽 바텀 왼쪽
        self.label3.setAlignment(Qt.AlignCenter)

        self.edit = QLineEdit(self)
        self.edit.move(10,400)
        
        self.label4 = QLabel("성명",self)
        self.label4.move(310, 10)
        self.label4.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.label4.setBuddy(self.edit)


    def showWindow(self):
        self.setGeometry(100,100,800,500)
        self.setWindowTitle("QLabelStyleWindow")
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = QLabelStyleWindow()
    sys.exit(app.exec_())
