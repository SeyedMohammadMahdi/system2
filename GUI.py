from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.textEditor = None
        self.elevator1 = []
        self.elevator2 = []
        self.elevator3 = []
        self.initUI()

    # def button_clicked(self):
    #     self.label.setText("you pressed the button")
    #     self.update()

    def initUI(self):
        self.setGeometry(200, 100, 600, 700)
        self.setWindowTitle("Elevator")

        # self.label = QtWidgets.QLabel(self)
        # self.label.setText("my first label!")
        # self.label.move(200, 50)

        for i in range(15):
            self.elevator1.append(QtWidgets.QPushButton(self))
            self.elevator1[i].move(60, 430 - 30 * i)
            self.elevator1[i].setText("floor " + str(i+1))
            self.elevator1[i].setStyleSheet("background-color : #02c712")

        for i in range(15):
            self.elevator2.append(QtWidgets.QPushButton(self))
            self.elevator2[i].move(180, 430 - 30 * i)
            self.elevator2[i].setText("floor " + str(i+1))
            self.elevator2[i].setStyleSheet("background-color : #02c712")

        for i in range(15):
            self.elevator3.append(QtWidgets.QPushButton(self))
            self.elevator3[i].move(300, 430 - 30 * i)
            self.elevator3[i].setText("floor " + str(i+1))
            self.elevator3[i].setStyleSheet("background-color : #02c712")

        # self.b1.clicked.connect(self.button_clicked)

        self.textEditor = QTextEdit(self)
        self.textEditor.move(0, 500)
        self.textEditor.resize(600, 200)
        self.textEditor.setText("FLOOR ")

        self.textEditor.setReadOnly(True)

    def printInfo(self, info1, info2, info3):
        self.textEditor.append(info1)
        self.textEditor.append(info2)
        self.textEditor.append(info3)


    def elevatorPosition(self, position1, position2, position3):
        for i in range(15):
            self.elevator1[i].setStyleSheet("background-color : #02c712")
            self.elevator2[i].setStyleSheet("background-color : #02c712")
            self.elevator3[i].setStyleSheet("background-color : #02c712")

        self.elevator1[position1].setStyleSheet("background-color : red")
        self.elevator2[position2].setStyleSheet("background-color : red")
        self.elevator3[position3].setStyleSheet("background-color : red")

