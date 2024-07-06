import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

class QLabelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.showWindow()

    def initWindow(self):
        self.label1 = QLabel("Center",self) # 라벨 생성
        self.label1.move(10,10) # 위치 지정
        self.label1.resize(90,90) # 사이즈 지정
        self.label1.setStyleSheet("border : 1px solid black") # 스타일 지정  / css스타일을 따름
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2 = QLabel("Left",self) # 라벨 생성
        self.label2.move(110,10) # 위치 지정
        self.label2.resize(90,90) # 사이즈 지정
        self.label2.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label2.setAlignment(Qt.AlignLeft)

        self.label3 = QLabel("H Center",self) # 라벨 생성
        self.label3.move(210,10) # 위치 지정
        self.label3.resize(90,90) # 사이즈 지정
        self.label3.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label3.setAlignment(Qt.AlignHCenter)

        self.label4 = QLabel("V Center",self) # 라벨 생성
        self.label4.move(310,10) # 위치 지정
        self.label4.resize(90,90) # 사이즈 지정
        self.label4.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label4.setAlignment(Qt.AlignVCenter)

        self.label5 = QLabel("Right",self) # 라벨 생성
        self.label5.move(410,10) # 위치 지정
        self.label5.resize(90,90) # 사이즈 지정
        self.label5.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label5.setAlignment(Qt.AlignRight)

        self.label6 = QLabel("Top",self) # 라벨 생성
        self.label6.move(510,10) # 위치 지정
        self.label6.resize(90,90) # 사이즈 지정
        self.label6.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label6.setAlignment(Qt.AlignTop) # 위치 지정

        self.label7 = QLabel("Bottom",self) # 라벨 생성
        self.label7.move(610,10) # 위치 지정
        self.label7.resize(90,90) # 사이즈 지정
        self.label7.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label7.setAlignment(Qt.AlignBottom)

        self.label8 = QLabel("Top Right",self) # 라벨 생성
        self.label8.move(710,10) # 위치 지정
        self.label8.resize(90,90) # 사이즈 지정
        self.label8.setStyleSheet("border: 1px solid black") # 스타일 지정
        self.label8.setAlignment(Qt.AlignTop | Qt.AlignRight)
        

    def showWindow(self):
        self.setGeometry(100,100,800,500)
        self.setWindowTitle("QLabelWindow")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hwin = QLabelWindow()
    sys.exit(app.exec_())
