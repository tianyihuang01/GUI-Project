from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle('Demos')

        line_edit = QLineEdit() #输入框

        line_edit.setText("hello world") # 默认在输入框填写的文字
        # line_edit.setPlaceholderText("hello world") #占位符提示文字
        line_edit.selectAll() #全选输入框的文字
        line_edit.setReadOnly(True) #文字只读

        # line_edit.setEchoMode(QLineEdit.Password) #密码输入框，蒙住文字

        text = line_edit.text() # 提取输入框的内容
        # print('you typed: ' + text)

        # ------------------------------------------------------------

        label = QLabel()
        label.setText('<b>Hello world</b>') # 文字加粗<b>

        # ---------------------------------------------------------

        self.checkbox = QCheckBox() #勾选框
        self.checkbox.setText('click me!')
        # checkbox.setChecked(True) #是否默认勾选
        # self.checkbox.stateChanged.connect(self.selected) #判断是否勾选

        # --------------------------------------------------------

        self.combobox = QComboBox() #下拉菜单
        self.combobox.addItem('item 1')
        self.combobox.addItem('item 2')
        self.combobox.addItems(['Item3', 'Item4'])
        self.combobox.currentIndexChanged.connect(self.selected2) #判断选项+位置

        # ---------------------------------------------------------
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        # layout.addWidget(line_edit)
        # layout.addWidget(label)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)

        self.setLayout(layout)
        # self.setFocus()

    def selected(self):
        if self.checkbox.isChecked():
            print("YAY")
        else:
            print("NAN")

    def selected2(self):
        current_text = self.combobox.currentText()
        current_index = self.combobox.currentIndex()
        print(current_text + ' at the index ' + str(current_index))


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec()