import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class HelloWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("Hello",self)

        self.setGeometry(100,100,600,400)
        self.setWindowTitle('Hello Window')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = HelloWindow()
    sys.exit(app.exec_())