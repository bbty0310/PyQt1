import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class QPushButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.showWindow()

    def initWindow(self):
        self.button = QPushButton('New',self)
        self.button.resize(self.button.sizeHint()) # sizeHint : 사이즈를 유동적으로 변경
        self.button.move(30,60)
        self.button.setStyleSheet("background-color:gray")

    def mousePressEvent(self, e):
        self.button.setText("Press")
        self.button.setStyleSheet("background-color:green")

    def mouseReleaseEvent(self, e):
        self.button.setText("Release")
        self.button.setStyleSheet("background-color:red")
        
        
    def showWindow(self):
        self.setGeometry(100,100, 500,300)
        self.setWindowTitle('QPushButtonWindow')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = QPushButtonWindow()
    sys.exit(app.exec_())
