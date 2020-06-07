from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow #import statements
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): #New Class 

    def __init__(self, *args, **kwargs):  #init is defined 
        super(MainWindow, self).__init__(*args, **kwargs)  #super init is called from parent class

        self.setWindowTitle("Calculator")  #sets the window title
        self.NameLabel = QLabel("A Simple calculator",self) #Set the application title
        self.NameLabel.move(700,50)  #Move to a particular position
        self.NameLabel.setFixedSize(500,100)  #Set the height and width of the title
        self.NameLabel.setStyleSheet("font: 30pt Comic Sans MS")  #set fontStyle

app = QApplication([])    

window = MainWindow()
window.show()  #shows the main window

app.exec_()