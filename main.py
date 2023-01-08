import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel, QLineEdit, QFileDialog
from datetime import *
from PyQt5.QtGui import QPixmap
import random




class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'zapis/wczytywanie'
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.show()

 



class MyTabWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tab1, "Zapis danych")
        self.tabs.addTab(self.tab2, "Wytyczne danych")
        self.tabs.addTab(self.tab3, "Mapa")

 

        self.tab1.layout = QVBoxLayout(self)
        self.l = QLabel()
        self.l.setText("")
        self.tab1.layout.addWidget(self.l)
        self.tab1.setLayout(self.tab1.layout)
        self.textbox1 = QLineEdit(self.tab1)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,40)
        self.button1 = QPushButton('Zapisz', self.tab1)
        self.button1.clicked.connect(self.save1)
        self.button1.move(20,80)




        self.tab2.layout = QVBoxLayout(self)
        self.l = QLabel()
        self.tab2.layout.addWidget(self.l)
        self.tab2.setLayout(self.tab2.layout)
        self.button2 = QPushButton('Wczytaj', self.tab2)
        self.button2.clicked.connect(self.getfile)
        self.button2.move(20,80)
        self.label2 = QLabel(self.tab2)
        self.label2.move(20, 20)
        self.label2.resize(280,40)



        self.tab3.layout = QVBoxLayout(self)
        self.l = QLabel()
        self.l.setText("3")
        self.tab3.layout.addWidget(self.l)
        self.tab3.setLayout(self.tab3.layout)

 
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def save1(self):
        dt = datetime.now()
        time = dt.strftime("%H-%M-%S")
        lat = str(random.randint(40, 50))
        lng = str(random.randint(40, 50))
        with open (str(time) + '.txt', 'w') as f:
            f.write(self.textbox1.text() + ' ' + time + ' lat: ' + str(lat) + ' lng: ' + str(lng)  )
    
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Text files (*.txt)")
        ffile = fname[0]
        try:
            with open(ffile, 'r') as file:
                read = file.readline()
                split_text = read.split()
                note = split_text[0]
                timestp = split_text[1]
                lng = split_text[3]
                lat = split_text[5]
                self.label2.setText( "Notka: " + str(note) + "\n" + "Timestamp: " + str(timestp) + "\n" + "Dane dla mapy: " + str(lng) + ' ' + str(lat))
        except:
            self.label2.setText("Nie wybrano zadnego pliku!")

 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    