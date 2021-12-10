from PyQt5 import Qt as Q

class LineEdit(Q.QWidget):
    def __init__(self, text):
        super().__init__()
        self.label = Q.QLabel(text)
        self.label.setMinimumSize(40, 0)
        self.label.setAlignment(Q.Qt.AlignRight | Q.Qt.AlignVCenter)
        self.edit = Q.QLineEdit()
        layout = Q.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        self.setLayout(layout)


class Table1(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(("One", "Two", "Three"))
        # Create buttons
        self.one = LineEdit("One")
        self.two = LineEdit("Two")
        self.three = LineEdit("Three")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from table1")
        self.search_record = Q.QPushButton("Search by ...")
        self.remove_record = Q.QPushButton("Remove by ...")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.one)
        buttons_layout.addWidget(self.two)
        buttons_layout.addWidget(self.three)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)


class Table2(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(("One", "Two", "Three"))
        # Create buttons
        self.one = LineEdit("One")
        self.two = LineEdit("Two")
        self.three = LineEdit("Three")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from table2")
        self.search_record = Q.QPushButton("Search by ...")
        self.remove_record = Q.QPushButton("Remove by ...")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.one)
        buttons_layout.addWidget(self.two)
        buttons_layout.addWidget(self.three)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)


class Table3(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(("One", "Two", "Three"))
        # Create buttons
        self.one = LineEdit("One")
        self.two = LineEdit("Two")
        self.three = LineEdit("Three")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from table3")
        self.search_record = Q.QPushButton("Search by ...")
        self.remove_record = Q.QPushButton("Remove by ...")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.one)
        buttons_layout.addWidget(self.two)
        buttons_layout.addWidget(self.three)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)


class Table4(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(("One", "Two", "Three"))
        # Create buttons
        self.one = LineEdit("One")
        self.two = LineEdit("Two")
        self.three = LineEdit("Three")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from table4")
        self.search_record = Q.QPushButton("Search by ...")
        self.remove_record = Q.QPushButton("Remove by ...")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.one)
        buttons_layout.addWidget(self.two)
        buttons_layout.addWidget(self.three)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)

class Ui(Q.QMainWindow):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.resize(900, 600)
        self.central_widget = Q.QWidget()
        MainWindow.setCentralWidget(self.central_widget)
        # Open data base
        self.open_db_label = Q.QLabel("Open database")
        self.open_db_edit = Q.QLineEdit()
        self.open_db_button = Q.QPushButton("Open")
        # Delete data base
        self.delete_db_button = Q.QPushButton("Delete database")
        # Delete all records
        self.remove_all_button = Q.QPushButton("Remove all records")
        # Tab widget
        self.tabs = Q.QTabWidget()
        self.tabs.addTab(Table1(), "table1")
        self.tabs.addTab(Table2(), "table2")
        self.tabs.addTab(Table3(), "table3")
        self.tabs.addTab(Table4(), "table4")
        # Set layout
        main_layout = Q.QGridLayout()
        main_layout.addWidget(self.open_db_label, 0, 0)
        main_layout.addWidget(self.open_db_edit, 0, 1)
        main_layout.addWidget(self.open_db_button, 0, 2)
        main_layout.addWidget(self.delete_db_button, 0, 3)
        main_layout.addWidget(self.remove_all_button, 1, 2, 1, 2)
        main_layout.addWidget(self.tabs, 2, 0, 1, 4)
        self.central_widget.setLayout(main_layout)


        
