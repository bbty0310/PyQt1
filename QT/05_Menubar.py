import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 600)
        self.setWindowTitle('메뉴바 툴바 상태바')
        self.menubar()
        self.toolbar()
        self.statusbar()
        self.show()

    def menubar(self):
        menubar = self.menuBar()
        Filemenu = menubar.addMenu('File')
        Editmenu = menubar.addMenu('Edit')
        Helpmenu = menubar.addMenu('Help')

        menubar.setStatusTip('메뉴바')

    def toolbar(self):
        quit_action = QAction(QIcon('image/exit.png'), 'Exit', self)
        quit_action.setShortcut('Ctrl+x')
        quit_action.setStatusTip('프로그램종료')
        quit_action.triggered.connect(qApp.quit) 
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(quit_action)
        self.toolbar.setStatusTip('툴바')

    def statusbar(self):
        self.statusBar().showMessage("상태표시줄이 준비되었습니다.") 

if __name__=='__main__':
    app = QApplication(sys.argv)
    hwin = MyBar()
    sys.exit(app.exec_())       