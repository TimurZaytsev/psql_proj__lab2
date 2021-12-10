import sys
from PyQt5 import Qt as Q
from gui import Ui

class MainWindow(Q.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = Q.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

