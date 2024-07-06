from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
import sys

class Absolutelayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button1 = QPushButton('버튼1',self)
        self.button2 = QPushButton('버튼2',self)
        
        # 좌우의 비율 조절 레이아웃
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addStretch(2)

        # 상하의 비율 조절 레이아웃
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        

        self.resize(600,300)
        self.setWindowTitle("상대 레이아웃")
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = Absolutelayout()
    sys.exit(app.exec_())