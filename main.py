import database as db
import sys
from PyQt5 import Qt as Q
from gui import Ui


if __name__ == '__main__':
    database = db.DatabasePy()
    #database.create_db("testing")
    #database.test_1_step()
    #database.drop_db()


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
