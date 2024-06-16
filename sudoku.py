import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QTableWidget, QTableWidgetItem
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QColor

difficulty = 10 # Adjust this to control the number of empty cells

def generate_sudoku():
    n = 9
    sudoku = [[0 for _ in range(n)] for _ in range(n)]
    fill_sudoku(sudoku)

    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for i in range(n):
        for j in range(n):
            cell_value = sudoku[i][j]
            if cell_value != 0:
                sudoku[i][j] = numbers[cell_value - 1]

    empty_grid_sudoku(sudoku)

    return sudoku

# Remove numbers to create the puzzle (adjust the difficulty by changing the number of removals)
def empty_grid_sudoku(grid):
    global difficulty 
    cells_to_remove = random.sample(range(81), difficulty)
    
    for cell in cells_to_remove:
        row, col = divmod(cell, 9)
        grid[row][col] = 0
    return 


def fill_sudoku(grid):
    if not find_empty(grid):
        return True
    row, col = find_empty(grid)
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if fill_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid_move(grid, row, col, num):
    return not (used_in_row(grid, row, num) or used_in_col(grid, col, num) or used_in_box(grid, row - row % 3, col - col % 3, num))

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    return num in [grid[i][col] for i in range(9)]

def used_in_box(grid, start_row, start_col, num):
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return True
    return False

class Ui_Form(object):
    def setupUi(self, Form):
        #Ui for 9x9
        Form.setObjectName("Form")
        Form.resize(480, 640)
        self.pushButton_Mark = QtWidgets.QPushButton(Form)
        self.pushButton_Mark.setGeometry(QtCore.QRect(290, 5010, 89, 25))
        self.pushButton_Mark.setObjectName("pushButton_Mark")
        self.pushButton_Undo = QtWidgets.QPushButton(Form)
        self.pushButton_Undo.setGeometry(QtCore.QRect(290, 5040, 89, 25))
        self.pushButton_Undo.setObjectName("pushButton_Undo")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(380, 4400, 26, 20))
        self.toolButton.setObjectName("toolButton")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(270, 50, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.time = QtWidgets.QLabel(Form)
        self.time.setGeometry(QtCore.QRect(260, 75, 51, 16))
        self.time.setObjectName("time")
        self.time_hours = QtWidgets.QLabel(Form)
        self.time_hours.setGeometry(QtCore.QRect(300, 75, 21, 16))
        self.time_hours.setObjectName("time_hours")
        self.time_dots = QtWidgets.QLabel(Form)
        self.time_dots.setGeometry(QtCore.QRect(318, 75, 21, 16))
        self.time_dots.setObjectName("time_dots")
        self.time_minutes = QtWidgets.QLabel(Form)
        self.time_minutes.setGeometry(QtCore.QRect(322, 75, 21, 16))
        self.time_minutes.setObjectName("time_minutes")
        self.time_dots_2 = QtWidgets.QLabel(Form)
        self.time_dots_2.setGeometry(QtCore.QRect(339, 75, 21, 16))
        self.time_dots_2.setObjectName("time_dots_2")
        self.time_second = QtWidgets.QLabel(Form)
        self.time_second.setGeometry(QtCore.QRect(343, 75, 21, 16))
        self.time_second.setObjectName("time_second")

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(235, 550, 161, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_Hint = QtWidgets.QPushButton(Form)
        self.pushButton_Hint.setGeometry(QtCore.QRect(290, 5070, 89, 25))
        self.pushButton_Hint.setObjectName("pushButton_Hint")
##        self.frame = QtWidgets.QFrame(Form)
##        self.frame.setGeometry(QtCore.QRect(60, 39, 361, 71))
##        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
##        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
##        self.frame.setObjectName("frame")
##        self.frame.raise_()
        self.pushButton_Mark.raise_()
        self.pushButton_Undo.raise_()
        self.toolButton.raise_()
        self.title.raise_()
        self.time.raise_()
        self.time_hours.raise_()
        self.time_dots.raise_()
        self.time_minutes.raise_()
        self.time_dots_2.raise_()
        self.time_second.raise_()
        self.gridLayoutWidget.raise_()
        self.pushButton_Hint.raise_()
        
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setGeometry(QtCore.QRect(60, 100, 510, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.setContentsMargins(0, 0, 0, 0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.cell_history = []  # Initialize an empty list to store cell history
        self.move_history = []  # Initialize a list to store move history
        self.current_state = []  # Initialize the current state
        self.current_move_index = 0  # Initialize the current move index
        self.selected_cell = None  # Initialize the selected cell
        self.cell_selected = False  #
        self.table_history = []

        self.selected_cell = None  # Initialize the selected cell
        self.cell_selected = False  # Initialize the flag
        
        self.initial_empty_cells = set()
        self.initUI()
        self.checking_valid_solution = False 
        self.game_over = False
        
         # Initialize a QTimer for checking the Sudoku solution
        self.timer = QTimer(Form)
        self.timer.timeout.connect(self.check_sudoku)  # Connect the timer to a function
        self.timer.start(1000)  # Start the timer with a 1-second interval (1000 milliseconds)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Mark.setText(_translate("Form", "Mark"))
        self.pushButton_Undo.setText(_translate("Form", "Undo"))
        self.pushButton_Hint.setText(_translate("Form", "Hint (3)"))
        self.toolButton.setText(_translate("Form", "..."))
        self.title.setText(_translate("Form", "SUDOKU"))
        self.time.setText(_translate("Form", "Time:"))
        self.time_hours.setText(_translate("Form", "00"))
        self.time_dots.setText(_translate("Form", ":"))
        self.time_minutes.setText(_translate("Form", "00"))
        self.time_dots_2.setText(_translate("Form", ":"))
        self.time_second.setText(_translate("Form", "00"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))

    def set_cell_value(self, number):
        if self.selected_cell:
            row, col = self.selected_cell
            item = QtWidgets.QTableWidgetItem(str(number))
            self.tableWidget.setItem(row, col, item)

    def on_cell_clicked(self, row, col):
        # Capture the current cell's row and column when a cell is clicked
        self.selected_cell = (row, col)
        self.cell_selected = True

    def initUI(self):    
        # Generate a Sudoku puzzle
        sudoku = generate_sudoku()

       # initial_empty_cells = set()
        x = 0
        global difficulty

        # Populate the table widget with Sudoku values
        for row in range(9):
            for col in range(9):
                num = sudoku[row][col]
                item = QTableWidgetItem(str(sudoku[row][col]))
                self.tableWidget.setItem(row, col, item)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                if num == 0 and x<difficulty:
                    self.initial_empty_cells.add((row, col))
                    x = x + 1

        for row, col in self.initial_empty_cells:
            item = self.tableWidget.item(row, col)
            item.setBackground(QColor("lightgrey"))
                    

        item = self.tableWidget.item(row, col)    
        self.pushButton_1.clicked.connect(lambda: self.set_cell_value(1) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_2.clicked.connect(lambda: self.set_cell_value(2) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_3.clicked.connect(lambda: self.set_cell_value(3) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_4.clicked.connect(lambda: self.set_cell_value(4) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_5.clicked.connect(lambda: self.set_cell_value(5) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_6.clicked.connect(lambda: self.set_cell_value(6) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_7.clicked.connect(lambda: self.set_cell_value(7) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_8.clicked.connect(lambda: self.set_cell_value(8) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.pushButton_9.clicked.connect(lambda: self.set_cell_value(9) if self.tableWidget.currentItem().background().color() == QColor("lightgrey") else None)
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
              
        self.check_valid_sudoku(sudoku)

        # Initialize the game timer
        self.elapsed_time = QDateTime(2000, 1, 1, 0, 0, 0)
        self.timer = QTimer(Form)
        self.timer.timeout.connect(self.update_game_timer)

        #background refresh timer
        self.color_timer = QTimer(Form)
        self.color_timer.timeout.connect(self.set_cells_background)
        self.color_timer.start(100)

        self.start_game()

        self.pushButton_1.clicked.connect(lambda: self.on_push_button_clicked(1))
        self.pushButton_2.clicked.connect(lambda: self.on_push_button_clicked(2))
        self.pushButton_3.clicked.connect(lambda: self.on_push_button_clicked(3))
        self.pushButton_4.clicked.connect(lambda: self.on_push_button_clicked(4))
        self.pushButton_5.clicked.connect(lambda: self.on_push_button_clicked(5))
        self.pushButton_6.clicked.connect(lambda: self.on_push_button_clicked(6))
        self.pushButton_7.clicked.connect(lambda: self.on_push_button_clicked(7))
        self.pushButton_8.clicked.connect(lambda: self.on_push_button_clicked(8))
        self.pushButton_9.clicked.connect(lambda: self.on_push_button_clicked(9))

        self.resize_table_columns(self.tableWidget, 40)

    def resize_table_columns(self, table_widget, width):
        for col in range(table_widget.columnCount()):
            table_widget.setColumnWidth(col, width)

    

#Cells Background Refresh#
    def set_cells_background(self):
        tableWidget = self.tableWidget
        initial_empty_cells = self.initial_empty_cells
        for row, col in initial_empty_cells:
            item = tableWidget.item(row, col)
            item.setBackground(QColor("lightgrey"))
            
#Game Timer#
    def start_game(self):
        self.start_time = QDateTime.currentDateTime()
        self.timer.start(1000)  # Start the timer with a 1-second interval

    def update_game_timer(self):
        if self.start_time is not None:
            current_time = QDateTime.currentDateTime()
            elapsed_time = self.start_time.secsTo(current_time)  # Elapsed time in seconds
            hours = elapsed_time // 3600  # Calculate hours
            minutes = (elapsed_time // 60) % 60  # Calculate remaining minutes
            seconds = elapsed_time % 60  # Calculate remaining seconds
            self.update_timer_display(hours, minutes, seconds)

    def update_timer_display(self, hours=0, minutes=0, seconds=0):
        if not self.game_over:  # Check the game_over flag
            self.time_hours.setText(f"{hours:02d}")  # Assuming you have a label for hours
            self.time_minutes.setText(f"{minutes:02d}")
            self.time_second.setText(f"{seconds:02d}")

#Checking Answer Validity#
    def check_sudoku(self):
        sudoku = self.get_sudoku_from_table()  # Get the current state of the Sudoku grid from the table
        if self.check_valid_sudoku(sudoku):
            self.timer.stop()  # Stop the timer if a valid solution is found
            self.game_over = True  # Set the game_over flag to True

    def get_sudoku_from_table(self):
        sudoku = []
        for row in range(9):
            row_data = []
            for col in range(9):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    value = int(item.text()) if item.text().isdigit() else 0
                    row_data.append(value)
            sudoku.append(row_data)
        return sudoku

    def check_valid_sudoku(self, sudoku):
        def is_valid_sudoku(grid):
            for i in range(9):
                if not is_valid_row(grid, i) or not is_valid_col(grid, i) or not is_valid_box(grid, i):
                    return False
            return True

        def is_valid_row(grid, row):
            seen = set()
            for num in grid[row]:
                if num == 0:
                    return False
                if num in seen:
                    return False
                seen.add(num)
            return True

        def is_valid_col(grid, col):
            seen = set()
            for row in range(9):
                num = grid[row][col]
                if num == 0:
                    return False
                if num in seen:
                    return False
                seen.add(num)
            return True

        def is_valid_box(grid, box):
            seen = set()
            start_row, start_col = 3 * (box // 3), 3 * (box % 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    num = grid[i][j]
                    if num == 0:
                        return False
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        if is_valid_sudoku(sudoku):
            if is_valid_sudoku:
                QMessageBox.information(None,"Sudoku Solved!")
                print("Valid Sudoku Solution")
            return True
        return False
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



