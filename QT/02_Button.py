import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QCoreApplication

class HelloWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("Hello",self)

        self.setGeometry(200,500,600,400)
        self.setWindowTitle('Hello Window')
        self.show()

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Hello exit",self)
        self.button.resize(self.button.sizeHint()) # 사이즈 재설정
        self.button.move(30,60) # 위치 조정

        self.setGeometry(200,500,600,400)
        self.button.setToolTip("이것은 <font color='red'> 종료 버튼</font>입니다") # 버튼에 마우스를 오래 두면 나오는 알람창, html 태그 사용 가능
        self.button.clicked.connect(QCoreApplication.instance().quit) # 클릭시 일어나는 이벤트 
        self.show() # 프로그램 창 실행


if __name__=='__main__':
    app = QApplication(sys.argv)
    # hwin = HelloWindow()
    bwin = ButtonWindow()
    sys.exit(app.exec_()) # 프로그램 종료 시 같이 종료