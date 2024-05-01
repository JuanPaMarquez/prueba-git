import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt6.QtGui import QFont
from PyQt6 import QtGui, QtCore
import threading
import time

globalTexto = "Ventana 1"

class inicio (QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()
        self.InicializarUI2()

    def InicializarUI(self):
        self.setGeometry(500, 100, 300, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def InicializarUI2(self):
        self.setGeometry(500, 100, 300, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        fondo = QVBoxLayout()
        titulo_inicial = QLabel(globalTexto)
        titulo_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_inicial.setStyleSheet("""QLabel {
                                     font-size: 30px;
                                     }""")
        fondo.addWidget(titulo_inicial)
        self.setLayout(fondo)



class inicio2 (QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()
        self.InicializarUI2()

    def InicializarUI(self):
        self.setGeometry(500, 100, 300, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def InicializarUI2(self):
        self.setGeometry(500, 100, 300, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        fondo = QVBoxLayout()
        titulo_inicial = QLabel("Ventana 2")
        titulo_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_inicial.setStyleSheet("""QLabel {
                                     font-size: 30px;
                                     }""")
        
        boton = QPushButton("boton 2")
        boton.clicked.connect(cambiar)

        fondo.addWidget(titulo_inicial)
        fondo.addWidget(boton)
        self.setLayout(fondo)
    
def cambiar():
    global globalTexto
    globalTexto = "Ventana 3"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = inicio()
    Login2 = inicio2()
    sys.exit(app.exec())
