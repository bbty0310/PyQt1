import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle('MyWindow')
        self.show()

    def closeEvent(self, QCloseEvent):
        answer = QMessageBox.question(self,
                                      '종료 msgbox', # msg title
                                      '종료하시겠습니까?', # msg
                                      QMessageBox.Yes | QMessageBox.No, # Yes or No
                                      QMessageBox.Yes) # default value
        if answer == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = MyWindow()
    sys.exit(app.exec_())