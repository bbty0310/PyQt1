import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class QPushButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.showWindow()

    def initWindow(self):
        self.button = QPushButton(self)
        self.button.setText("btnMouse hovor pressed")
        self.button.setGeometry(100,100,200,40)
        # 클릭시 색 반응 작용
        self.button.setStyleSheet("QPushButton::hovor"
                                  "{"
                                  "background-color: yellow;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color: red;"
                                  "}")
        
    def showWindow(self):
        self.setGeometry(100,100, 500,300)
        self.setWindowTitle('QPushButtonWindow')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = QPushButtonWindow()
    sys.exit(app.exec_())
