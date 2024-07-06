from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QGridLayout
import sys

class Absolutelayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button1 = QPushButton('버튼1',self)
        self.button1.move(100,100)
        self.button2 = QPushButton('버튼2',self)
        self.button2.move(100,200)

        self.resize(600,300)
        self.setWindowTitle("절대 레이아웃")
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = Absolutelayout()
    sys.exit(app.exec_())