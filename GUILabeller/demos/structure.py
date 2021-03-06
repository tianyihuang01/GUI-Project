from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # layout = QVBoxLayout() # vertical layout
        # layout = QHBoxLayout() # horizontal layout
        layout = QGridLayout() # grid layout

        self.label = QLabel('Hello World!')
        line_edit = QLineEdit()
        button = QPushButton('Close')

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        # line_edit.textChanged.connect(label.setText)
        line_edit.textChanged.connect(self.changeTextLabel)

        # self.connect(line_edit, SIGNAL('TextChanged(QString)'), self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec()
