import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

class MyBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600,300)
        self.setWindowTitle("Center window")
        self.CenterWindow()
        self.show()

    def CenterWindow(self):
        f_geo = self.frameGeometry()
        print(f_geo)
        center_pos = QDesktopWidget().availableGeometry().center()
        f_geo.moveCenter(center_pos)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex= MyBar()
    sys.exit(app.exec_())