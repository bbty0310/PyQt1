import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QCoreApplication

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("버튼 클릭",self)
        self.button.resize(self.button.sizeHint()) # 버튼 클릭 횟수 설정
        self.button.move(30,60) # 버튼 위치 

        
        self.button.setToolTip("이 버튼을 클릭해주세요") # 버튼에 마우스를 오래 두면 나오는 알람창, html 태그 사용 가능
        self.button.clicked.connect(self.click) # 클릭시 일어나는 이벤트 

        self.nclick = 0
        self.label = QLabel(self)
        self.label.setText(f"Button Clicked : {self.nclick}")

        self.label.move(30,90)

        self.setGeometry(200,500,600,400)
        self.setWindowTitle("클릭 버튼 윈도우")

        self.show() # 프로그램 창 실행

    def click(self):
        print("Button clicked")
        self.nclick += 1
        self.show_clicked_count(self.nclick)

    def show_clicked_count(self, ncount):
        self.label.setText(f"버튼 클릭횟수 : {ncount}")
        self.label.resize(self.label.sizeHint())
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    # hwin = HelloWindow()
    bwin = ButtonWindow()
    sys.exit(app.exec_()) # 프로그램 종료 시 같이 종료