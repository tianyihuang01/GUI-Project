from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
from pathlib import Path
import subprocess

dev = []
# save_dir = ""
package_name = ""
save_file = ""


class Labeller(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        layout = QGridLayout()

        # self.label_check = QLabel('Check emulators:')
        self.button_check = QPushButton('1. Check Emulators')
        self.label_check_result = QLabel('...')
        # self.edit_check_result = QLineEdit('...')
        # self.edit_check_result.setReadOnly(True)

        self.button_package_1 = QPushButton('2. Check Name 1')
        self.edit_package_1_result = QLineEdit('...')
        self.edit_package_1_result.setReadOnly(True)
        self.button_package_2 = QPushButton('3. Check Name 2')
        self.edit_package_2_result = QLineEdit('...')
        self.edit_package_2_result.setReadOnly(True)

        self.button_location = QPushButton('4. Save Location')
        self.edit_location_result = QLineEdit('D:\Desktop\GUITest')

        self.button_location_o = QPushButton('Open location')
        # self.button_location_o.setFixedWidth(fm.boundingRect(text).width() + 6)

        self.button_save = QPushButton('*Get n Save*')

        self.label_issue = QLabel('login issue? ')
        self.button_tag_phone = QPushButton('phone')
        self.button_tag_tv = QPushButton('tv')
        button_close = QPushButton('Close')

        # layout.addWidget(self.label_check, 0, 0)
        layout.addWidget(self.button_check, 0, 0)
        layout.addWidget(self.label_check_result, 0, 1)
        # layout.addWidget(self.edit_check_result, 0, 1)
        layout.addWidget(self.button_package_1, 1, 0)
        layout.addWidget(self.edit_package_1_result, 1, 1)
        layout.addWidget(self.button_package_2, 2, 0)
        layout.addWidget(self.edit_package_2_result, 2, 1)
        layout.addWidget(self.button_location, 3, 0)
        layout.addWidget(self.edit_location_result, 3, 1)
        layout.addWidget(self.button_location_o, 4, 0)
        layout.addWidget(self.button_save, 6, 0)
        layout.addWidget(self.label_issue, 7, 0)
        layout.addWidget(self.button_tag_phone, 8, 0)
        layout.addWidget(self.button_tag_tv, 8, 1)
        layout.addWidget(button_close, 9, 1)


        self.setLayout(layout)
        self.setWindowTitle('GUI Labeller')
        self.setFocus()

        button_close.clicked.connect(self.close)

        self.button_check.clicked.connect(self.check_device)

        # https://blog.csdn.net/flhsxyz/article/details/79220936
        self.button_package_1.clicked.connect(lambda: self.check_package(1))
        self.button_package_2.clicked.connect(lambda: self.check_package(2))

        self.button_location.clicked.connect(self.browse_file)

        self.button_location_o.clicked.connect(self.open_file)

        self.button_save.clicked.connect(self.save_gui)

        self.button_tag_phone.clicked.connect(lambda: self.tag('phone'))
        self.button_tag_tv.clicked.connect(lambda: self.tag('tv'))

    def check_device(self):
        # os.system('adb devices')
        # https://stackoverflow.com/questions/18739239/python-how-to-get-stdout-after-running-os-system/26343770
        r = str(subprocess.check_output('adb devices', shell=True))
        r = r[2:-1]
        r = r.replace('\\r\\n', '<br/>')
        r = r.replace("\\t", " ")
        # self.edit_check_result.setText(str(r))
        self.label_check_result.setText(str(r))

        dev_count = r.count('<br/>')-2 # number of adb devices
        # print(dev_count)
        dev.clear()

        if dev_count >= 1:
            dev.append(r.split('<br/>')[1].split(" ")[0])
            # print(dev_1)
            if dev_count == 2:
                dev.append(r.split('<br/>')[2].split(' ')[0])
                # print(dev_2)
        print(dev)

    def check_package(self, number):
        cmd = str()
        if len(dev) == 1:
            cmd = 'adb shell dumpsys window windows | find "mCurrentFocus"'
        elif len(dev) >= 2:
            if number == 1:
                cmd = 'adb -s ' + dev[0] + ' shell dumpsys window windows | find "mCurrentFocus"'
                print(cmd)
            if number == 2:
                cmd = 'adb -s ' + dev[1] + ' shell dumpsys window windows | find "mCurrentFocus"'
                print(cmd)

        r = str(subprocess.check_output(cmd,shell=True))
        package_details = r.split(" ")[-1].split("/")
        global package_name
        package_name = package_details[0]
        activity_name = package_details[-1][0:-1]
        if number == 1:
            self.edit_package_1_result.setText(str(package_name))
        elif number == 2:
            self.edit_package_2_result.setText(str(package_name))

    def browse_file(self):
        # global save_dir #一定要加上这个，否则save_dir全局变量无法赋值
        # https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog
        save_dir = QDir.toNativeSeparators(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        print(save_dir)
        self.edit_location_result.setText(save_dir)

    def open_file(self):
        # print(save_dir)
        save_dir = self.edit_location_result.text()
        os.startfile(save_dir)


    def save_gui(self):
        global save_file
        # global package_name
        package_name_1 = self.edit_package_1_result.text()
        package_name_2 = self.edit_package_2_result.text()
        save_file = self.edit_location_result.text() + "\\" + package_name_1
        # https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
        Path(save_file).mkdir(parents=True, exist_ok=True)

        # check the existed folder
        # https://stackoverflow.com/questions/29769181/count-the-number-of-folders-in-a-directory-and-subdirectories
        folders = 0
        for root, dirs, files in os.walk(save_file):
            folders += len(dirs)
        print(folders)
        save_file = save_file + "\\" + str(folders+1)
        print(save_file)
        Path(save_file).mkdir(parents=True, exist_ok=True)

        cmd = []
        if len(dev) == 1:
            cmd_1 = 'adb exec-out screencap -p > ' + save_file + '\\screen1_' + package_name_1 + '.png'
            cmd_2 = 'adb exec-out uiautomator dump /dev/tty > ' + save_file + '\\screen1_' + package_name_1 + '.xml'
            cmd.extend([cmd_1, cmd_2])
        if len(dev) == 2:
            cmd_0_0 = "adb -s " + dev[0]
            cmd_0_1 = "adb -s " + dev[1]
            cmd_1 = cmd_0_0 + ' exec-out screencap -p > ' + save_file + '\\screen1_' + package_name_1 + '.png'
            cmd_2 = cmd_0_0 + ' exec-out uiautomator dump /dev/tty > ' + save_file + '\\screen1_' + package_name_1 + '.xml'
            cmd_3 = cmd_0_1 + ' exec-out screencap -p > ' + save_file + '\\screen2_' + package_name_2 + '.png'
            cmd_4 = cmd_0_1 + ' exec-out uiautomator dump /dev/tty > ' + save_file + '\\screen2_' + package_name_2 + '.xml'
            cmd.extend([cmd_1, cmd_2, cmd_3, cmd_4])

        print(cmd)

        # run the command.
        for cmd_e in cmd:
            subprocess.check_output(cmd_e, shell=True)

        # show success dialog
        QMessageBox.information(self, 'Complete', 'The GUI labelling is complete!')

    def tag(self, device):
        global save_file
        # global package_name
        package_name_1 = self.edit_package_1_result.text()
        package_name_2 = self.edit_package_2_result.text()
        save_file = self.edit_location_result.text() + "\\" + package_name_1
        # https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
        Path(save_file).mkdir(parents=True, exist_ok=True)
        # create tag files
        if device == 'phone':
            f = open(save_file + '\\login_issue_phone_' + package_name_1 + '.txt', 'w')
            f.write('The phone app cannot log in')
            f.close()
        if device == 'tv':
            f = open(save_file + '\\login_issue_tv_' + package_name_1 + '.txt', 'w')
            f.write('The tv app cannot log in')
            f.close()

        # show success dialog
        QMessageBox.information(self, 'Complete', 'The login issue is tagged!')


app = QApplication(sys.argv)
dialog = Labeller()
dialog.show()
app.exec()