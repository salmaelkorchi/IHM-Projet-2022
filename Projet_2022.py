#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:27:15 2022

@author: selmael-korchi
"""


import sys 

from PyQt5.QtWidgets import (QLineEdit, QTextEdit, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout,
                              QApplication, QMainWindow, QWidget)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import dbm

dbmfile = dbm.open('MedicalFollowUpDataBase','c') 

# class patient (self):
#     self.patient = patient
#     self.ln = Last_name
#     self.fn = First_Name
#     self.age = Age
#     self.s = Sexe

class View2(QWidget):
    def __init__(self, ctrl):
        super().__init__()
                
        self.CONTROLLER = ctrl
        
        self.patient = []
        
        self.b3 = QPushButton('History')
        self.b4 = QPushButton('Save')
        self.b5 = QPushButton('Cancel')
                
        self.txt1 = QLineEdit('')
        self.txt2 = QLineEdit('')
        self.txt3 = QLineEdit('')
                
        self.txt4 = QLineEdit('')
        self.txt5 = QLineEdit('')
                
        self.rbtn1 = QRadioButton('M')
        self.rbtn2 = QRadioButton('F')
        self.label5 = QLabel("Sexe")

        
        self.label2 = QLabel("Last Name")
        self.label3 = QLabel("First Name")
        self.label4 = QLabel("Age")
      
        self.init_ui() 
                
        self.show() 
                
    def init_ui(self):
        self.setStyleSheet("background-color:lightgrey")  
                
        layout = QVBoxLayout()
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
                
        h_box = QVBoxLayout()
        v_box = QHBoxLayout()
        h_box.addWidget(self.label2)
        h_box.addWidget(self.txt1)
        h_box.addWidget(self.label3)
        h_box.addWidget(self.txt2)
        h_box.addWidget(self.label4)
        h_box.addWidget(self.txt3)
        h_box.addWidget(self.label5)
        h_box.addWidget(self.rbtn1)
        h_box.addWidget(self.rbtn2)
        h_box.addWidget(self.b4)


        v_box = QHBoxLayout()
        v_box.addLayout(h_box) 
        v_box.addWidget(self.txt4)
        v_box.addWidget(self.txt5)
        v_box.addWidget(self.b3)
        v_box.addWidget(self.b5)

 
        self.setLayout(v_box)
        self.setWindowTitle('Medical Follow Up')
        self.setGeometry(500, 300, 500, 300)

        self.txt1.setDisabled(False)
        self.txt1.setStyleSheet("background-color:white;color:black")
                
        self.txt2.setDisabled(False)
        self.txt2.setStyleSheet("background-color:white;color:black")
        
        self.txt3.setDisabled(False)
        self.txt3.setStyleSheet("background-color:white;color:black")
                
        self.txt4.setDisabled(True)
        self.txt4.setStyleSheet("background-color:white;color:black")
                
        self.txt5.setDisabled(False)
        self.txt5.setStyleSheet("background-color:white;color:black")
    
        self.b3.clicked.connect(self.btn3_click) 
        self.b3.setStyleSheet("background-color:blue;color:white")

        # self.b4.clicked.connect(self.btn4_click) 
        self.b4.setStyleSheet("background-color:blue;color:white")
       
        # self.b5.clicked.connect(self.btn5_click) 
        self.b5.setStyleSheet("background-color:blue;color:white")
        
        # self.rbtn1.toggled.connect(self.onClicked)
        # self.rbtn2.toggled.connect(self.onClicked)
        
    def btn3_click(self, patient):
        self.CONTROLLER.saveP(self.patient.text()) 
        
    # def btn5_click(self):
    #     self.close(View1)
    # def btn4_click(self):
    #     self.v1 = View1
        # self.v1.show()
        # self.hide()
        
class View1(QWidget):
    def __init__(self):
        super().__init__()
        
        # self.CONTROLLER = ctrl
        
        self.label1 = QLabel("Medical Follow Up")
        self.label2 = QLabel("Easy way to manage your patiens follow up !")
        self.b1 = QPushButton('New file')
        self.b2 = QPushButton('Import file')
        
        # self.pixmap = QPixmap('medical.jpg')
        # self.label = QLabel(self)
        # self.label.setPixmap(self.pixmap)
        
        self.init_ui() 
        
        self.show() 
        
    def init_ui(self):
        self.setStyleSheet("background-color:lightgrey")  
        
        h_box = QVBoxLayout()
        h_box.addWidget(self.label1)
        h_box.addWidget(self.label2)
        h_box.addWidget(self.b1)
        h_box.addWidget(self.b2)

        v_box = QHBoxLayout()
        v_box.addLayout(h_box) 
        
        self.setLayout(v_box)
        self.setWindowTitle('Medical Plateform')
        self.setGeometry(200, 200, 200, 200)

        
        self.label1.setStyleSheet("color:black;marging:25")
        self.label1.setAlignment(Qt.AlignCenter)        
        self.label2.setStyleSheet("color:black")
        self.label2.setAlignment(Qt.AlignCenter)        


        self.b1.clicked.connect(self.btn1_click) 
        self.b1.setStyleSheet("background-color:blue;color:white")

        # self.b2.clicked.connect(self.btn2_click) 
        self.b2.setStyleSheet("background-color:blue;color:white")      
        


        self.show() 

    def btn1_click(self):                                             
        self.v2 = View2(ctrl)
        self.v2.show()
        self.hide()  
        
    # def btn2_click(self):
        
    # def btn1_click(self): 
    #     self.CONTROLLER.fileN(self) 
        
    # def btn2_click(self): 
    #     self.aux = self.CONTROLLER.fileI()
    
 # %%   
class Controller:
    
    def __init__(self, model):
        self.MODEL = model 

   
    def addP(self, patient): 
        self.MODEL.addStudents(patient) 
     
    # def removeS(self, name): 
    #     self.MODEL.removeStudents(name)
    
    # def showS(self): 
    #     return self.MODEL.showStudents()
    
# %%    
class Model:
    def _init_(self):
        self.task = False 
        
    def savePatient(self, patient):
        dbmfile = dbm.open('MedicalFollowUpDataBase','c') 
        dbmfile[patient] = patient 
        self.task = True 
        dbmfile.close() 

    # def removeStudents(self, name):
    #     dbmfile = dbm.open('DataBaseStudents','c') 
    #     del dbmfile[name] 
    #     self.task = True 
    #     dbmfile.close() 
    
    # def showStudents(self):
    #     self.list = "" 
    #     dbmfile = dbm.open('DataBaseStudents','c') 
    #     for i in dbmfile.keys() : 
    #         self.list = self.list + ">" 
    #         self.list = self.list + str(dbmfile[i]) 
    #         self.list = self.list + "<" 
    #         self.list = self.list + "\n" 
    #     dbmfile.close() 
    #     return self.list 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    ctrl = Controller(model)
    View1 = View1()
    # View2 = View2(ctrl)
    sys.exit(app.exec())  