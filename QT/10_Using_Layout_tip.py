from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
import sys

class ApplicationLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       
       # EDIT
        self.edit = QLineEdit(self)
       
        #버튼
        self.button21 = QPushButton('10대',self)
        self.button22 = QPushButton('20대',self)
        self.button23 = QPushButton('30대',self)
        self.button31 = QPushButton('남자',self)
        self.button32 = QPushButton('여자',self)
       
        #라벨
        self.label1 = QLabel('이름', self)
        self.label2 = QLabel('나이', self)
        self.label3 = QLabel('성별', self)
        
        # 기본 레이아웃 설정 및 라벨 삽입
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.label1,0,0)
        grid.addWidget(self.label2,1,0)
        grid.addWidget(self.label3,2,0)
        grid.addWidget(self.edit,0,1)

        # 나이 관련 위젯 설정
        hbox_age = QHBoxLayout()
        hbox_age.addWidget(self.button21)
        hbox_age.addWidget(self.button22)
        hbox_age.addWidget(self.button23)
        grid.addLayout(hbox_age,1,1)

        # 성별 관련 위젯 설정
        hbox_gender = QHBoxLayout()
        hbox_gender.addWidget(self.button31)
        hbox_gender.addWidget(self.button32)
        grid.addLayout(hbox_gender,2,1)
        
        self.resize(300,100)
        self.setWindowTitle('Mixed layout')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = ApplicationLayout()
    sys.exit(app.exec_())