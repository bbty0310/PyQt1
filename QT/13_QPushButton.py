import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class QPushButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.showWindow()

    def initWindow(self):
        self.button1 = QPushButton(self)
        self.button1.setText('button&1 OFF') # & : 언더바 취해짐
        self.button1.setCheckable(True)
        self.button1.setStyleSheet("background-color:gray")
        self.button1.move(10,10)
        self.button1.toggled.connect(self.btnToggle)

        self.button2 = QPushButton(self)
        self.button2.setText('button2 단축기 ALT+F1')
        self.button2.move(10,40)
        self.button2.setCheckable(True)
        self.button2.setShortcut("ALT+F1")

    def btnToggle(self,state):
        print(state)
        self.button1.setStyleSheet("background-color:%s" % ({True:'red', False:'gray'}[state]))
        self.button1.setText({True:'button&1 ON', False:'button&1 OFF'}[state])

    def showWindow(self):
        self.setGeometry(100,100, 500,300)
        self.setWindowTitle('QPushButtonWindow 단축키')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = QPushButtonWindow()
    sys.exit(app.exec_())
