from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QGridLayout
import sys

class GridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 생성
        self.button1 = QPushButton('btn 1', self)
        self.button2 = QPushButton('btn 2', self)
        self.button3 = QPushButton('btn 3', self)
        
        # 라벨 생성
        self.label1 = QLabel('Name : ', self)
        self.label2 = QLabel('Age : ', self)
        self.label3 = QLabel('Gender : ', self)

        #그리드 레이아웃 생성 및 설정
        grid = QGridLayout()
        self.setLayout(grid)

        # 생성한 버튼&라벨 레이아웃에 부착
        grid.addWidget(self.label1,0,0) # (0,0) 자리에 생성
        grid.addWidget(self.label2,1,0)
        grid.addWidget(self.label3,2,0)
        grid.addWidget(self.button1,0,1)
        grid.addWidget(self.button2,1,1)
        grid.addWidget(self.button3,2,1)

        # 프로그램 사이즈 설정
        self.resize(300,100)
        # 타이틀 명 
        self.setWindowTitle('2 by 3 grid layout')
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hwin =GridLayout()
    sys.exit(app.exec_())