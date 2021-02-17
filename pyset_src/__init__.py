#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

import yaml

class PySet(QWidget):
    def __init__(self):
        super(PySet, self).__init__()
        layout = QVBoxLayout(self)
        welcomeLbl = QLabel("Welcome")
        welcomeLbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(welcomeLbl)
        installBtn = QPushButton("Install")
        layout.addWidget(installBtn)
        yamlCfg = self.yamlCfg = yaml.safe_load(open("pyset.yml", "r"))
        self.setWindowTitle(yamlCfg["name"] + " Installation")
        welcomeLbl.setText("Welcome to the installation of " + yamlCfg["name"])
        try:
            if(yamlCfg["pixmap"]):
                welcomeLbl.setPixmap(QPixmap(yamlCfg["pixmap"]))
        except KeyError:
            print("No pixmap")
        installBtn.clicked.connect(self.install)

    def install(self):
        print("Installing")
        os.system(f'xterm -e "cd {os.getcwd()}; {self.yamlCfg["command"]}; read -n1 -p \'Press any key to exit\'"')


def main():
    app = QApplication([])
    widget = PySet()
    widget.show()
    sys.exit(app.exec_())
