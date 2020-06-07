from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton #import statements
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QBrush,QPen

class MainWindow(QMainWindow): #New Class 

    def __init__(self, *args, **kwargs):  #init is defined 
        super(MainWindow, self).__init__(*args, **kwargs)  #super init is called from parent class

        self.setWindowTitle("Calculator")  #sets the window title
        self.NameLabel = QLabel("A Simple calculator",self) #Set the application title
        self.NameLabel.move(720,50)  #Move to a particular position
        self.NameLabel.setFixedSize(500,100)  #Set the height and width of the title
        self.NameLabel.setStyleSheet("font: 30pt Comic Sans MS")  #set fontStyle

        one = QPushButton('1', self) #the button '1'
        one.move(675,195)
        one.resize(125,200)
        one.setStyleSheet("font: 40px")

        two = QPushButton('2', self) #the button '2'
        two.move(800,195)
        two.resize(125,200)
        two.setStyleSheet("font: 40px")

        three = QPushButton('3', self) #the button '3'
        three.move(925,195)
        three.resize(125,200)
        three.setStyleSheet("font: 40px")

        four = QPushButton('4', self) #the button '4'
        four.move(675,395)
        four.resize(125,200)
        four.setStyleSheet("font: 40px")
   
        five = QPushButton('5', self) #the button '5'
        five.move(800,395)
        five.resize(125,200)
        five.setStyleSheet("font: 40px")

        six = QPushButton('6', self) #the button '6'
        six.move(925,395)
        six.resize(125,200)
        six.setStyleSheet("font: 40px")

        seven = QPushButton('7', self) #the button '7'
        seven.move(675,595)
        seven.resize(125,200)
        seven.setStyleSheet("font: 40px")

        eight = QPushButton('8', self) #the button '8'
        eight.move(800,595)
        eight.resize(125,200)
        eight.setStyleSheet("font: 40px")

        nine = QPushButton('9', self) #the button '9'
        nine.move(925,595)
        nine.resize(125,200)
        nine.setStyleSheet("font: 40px")

        plus = QPushButton('+', self) #the button '+'
        plus.move(1050,195)
        plus.resize(175,150)
        plus.setStyleSheet("font: 40px")

        minus = QPushButton('-', self) #the button '-'
        minus.move(1050,345)
        minus.resize(175,150)
        minus.setStyleSheet("font: 60px")

        multi = QPushButton('X', self) #the button 'X'
        multi.move(1050,495)
        multi.resize(175,150)
        multi.setStyleSheet("font: 40px")
        

        divide = QPushButton('/', self) #the button '/'
        divide.move(1050,645)
        divide.resize(175,150)
        divide.setStyleSheet("font: 40px")

        zero = QPushButton('0', self) #the button '0'
        zero.move(675,795)
        zero.resize(187.5,150)
        zero.setStyleSheet("font: 40px")

        equal = QPushButton('=', self) #the button '='
        equal.move(862.5,795)
        equal.resize(187.5,150)
        equal.setStyleSheet("font: 40px")

        lastres = QPushButton('Search for a saved calculation ', self) #the button 'saved calculations'
        lastres.move(1050,795)
        lastres.resize(175,150)
        lastres.setStyleSheet("font: 11px")
        

    def paintEvent(self,e):  #The coover of calculator
        painter = QPainter(self) #The initial outer cover of calculator
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine)) #setting the painter length
        painter.drawRect(650,170,600,800)    #set up a rectangle

        painter1 = QPainter(self) #The inner cover
        painter1.setPen(QPen(Qt.black, 5, Qt.SolidLine)) #setting the painter1 length
        painter1.drawRect(675,195,550,750)    #set up a rectangle  of painter1  

        painter2 = QPainter(self) #The number cover
        painter2.setPen(QPen(Qt.black, 5, Qt.SolidLine)) #setting the painter2 length
        painter2.drawRect(675,195,375,600)    #set up a rectangle of painter2

        painter3 = QPainter(self) #The sign cover
        painter3.setPen(QPen(Qt.black, 5, Qt.SolidLine)) #setting the painter3 length
        painter3.drawRect(1050,195,175,600)    #set up a rectangle of painter3   

        painter4 = QPainter(self) #covers 0 and =
        painter4.setPen(QPen(Qt.black, 5, Qt.SolidLine)) #setting the painter3 length
        painter4.drawRect(675,795,375,150)    #set up a rectangle of painter3   

        


app = QApplication([])    

window = MainWindow()
window.show()  #shows the main window

app.exec_()