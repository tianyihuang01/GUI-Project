from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
from pathlib import Path
import subprocess

dev = []
# save_dir = ""
package_name = []
activity_name = []
save_file = ""
apk_list = []
apk_index = -1

apk_path = 'D:\\Desktop\\GUITest'
save_path = 'D:\\Desktop\\GUIResult'


class Labeller(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QGridLayout()

        # self.label_check = QLabel('Check emulators:')
        self.button_check = QPushButton('1. Check Emulators')
        self.label_check_result = QLabel('...')
        # self.edit_check_result = QLineEdit('...')
        # self.edit_check_result.setReadOnly(True)

        self.label_em_1_id = QLabel('First emulator is: ')
        self.label_em_2_id = QLabel('Second emulator is:')
        self.combobox_em_1 = QComboBox()
        self.combobox_em_1.addItems(['phone', 'tv'])
        self.combobox_em_2 = QComboBox()
        self.combobox_em_2.addItems(['tv', 'phone'])


        self.button_apk = QPushButton('Apk Location')
        self.edit_apk_result = QLineEdit(apk_path)
        self.button_apk_o = QPushButton('Open location')

        self.button_apk_list = QPushButton('2. Check APK')
        self.label_apk_list = QLabel('......')

        self.button_next = QPushButton('3. Next App')
        self.label_package = QLabel('......')
        self.button_last = QPushButton('Last App')

        self.button_install = QPushButton('Install Apps')
        self.button_open = QPushButton('Launch Apps')
        self.button_uninstall = QPushButton('Uninstall Apps')

        self.label_emulator_1 = QLabel('Emulator 1')
        self.label_emulator_2 = QLabel('Emulator 2')

        self.button_package_1 = QPushButton('4. Check Packages: ')
        self.edit_package_1_result = QLineEdit('...')
        self.edit_package_1_result.setReadOnly(True)
        # self.button_package_2 = QPushButton('3. Check Name 2')
        self.edit_package_2_result = QLineEdit('...')
        self.edit_package_2_result.setReadOnly(True)

        self.button_location = QPushButton('Save Location')
        self.edit_location_result = QLineEdit(save_path)
        self.button_location_o = QPushButton('Open location')

        self.button_save = QPushButton('*Get n Save*')
        self.label_activity_1 = QLabel('activity name 1: ')
        self.label_activity_2 = QLabel('activity name 2: ')

        self.edit_activity_1_result = QLineEdit('...')
        self.edit_activity_1_result.setReadOnly(True)
        self.edit_activity_2_result = QLineEdit('...')
        self.edit_activity_2_result.setReadOnly(True)

        self.label_break = QLabel('...................................')
        self.label_break_1 = QLabel('...................................')

        self.label_issue_login = QLabel('login issue? ')
        self.button_tag_phone = QPushButton('phone')
        self.button_tag_tv = QPushButton('tv')

        self.label_issue_layout = QLabel('Same Layout? ')
        self.button_tag_layout = QPushButton('yes')

        button_close = QPushButton('Close')

        # layout.addWidget(self.label_check, 0, 0)
        layout.addWidget(self.button_check, 0, 0)
        layout.addWidget(self.label_check_result, 0, 1)
        # layout.addWidget(self.edit_check_result, 0, 1)

        layout.addWidget(self.label_em_1_id, 1, 0)
        layout.addWidget(self.combobox_em_1, 1, 1)
        layout.addWidget(self.label_em_2_id, 2, 0)
        layout.addWidget(self.combobox_em_2, 2, 1)

        layout.addWidget(self.button_apk, 3, 0)
        layout.addWidget(self.edit_apk_result, 3, 1)
        layout.addWidget(self.button_apk_o, 3, 2)

        layout.addWidget(self.button_apk_list, 4, 0)
        layout.addWidget(self.label_apk_list, 4, 1)

        layout.addWidget(self.button_next, 5, 0)
        layout.addWidget(self.label_package, 5, 1)
        layout.addWidget(self.button_last, 5, 2)

        layout.addWidget(self.button_install, 6, 0)
        layout.addWidget(self.button_open, 6, 1)
        layout.addWidget(self.button_uninstall, 6, 2)

        layout.addWidget(self.label_break_1, 10, 0)

        layout.addWidget(self.button_location, 11, 0)
        layout.addWidget(self.edit_location_result, 11, 1)
        layout.addWidget(self.button_location_o, 11, 2)

        layout.addWidget(self.label_emulator_1, 13, 1)
        layout.addWidget(self.label_emulator_2, 13, 2)

        layout.addWidget(self.button_package_1, 14, 0)
        layout.addWidget(self.edit_package_1_result, 14, 1)
        # layout.addWidget(self.button_package_2, 2, 0)
        layout.addWidget(self.edit_package_2_result, 14, 2)

        layout.addWidget(self.label_activity_1, 15, 1)
        layout.addWidget(self.label_activity_2, 15, 2)

        layout.addWidget(self.button_save, 16, 0)
        layout.addWidget(self.edit_activity_1_result, 16, 1)
        layout.addWidget(self.edit_activity_2_result, 16, 2)

        layout.addWidget(self.label_break, 17, 0)

        layout.addWidget(self.label_issue_login, 18, 0)
        layout.addWidget(self.button_tag_phone, 18, 1)
        layout.addWidget(self.button_tag_tv, 18, 2)

        layout.addWidget(self.label_issue_layout, 19, 0)
        layout.addWidget(self.button_tag_layout, 19, 1)

        layout.addWidget(button_close, 21, 2)

        self.setLayout(layout)
        self.setWindowTitle('GUI Labeller')
        self.setFocus()

        button_close.clicked.connect(self.close)

        self.button_check.clicked.connect(self.check_device)

        # https://blog.csdn.net/flhsxyz/article/details/79220936
        self.button_package_1.clicked.connect(self.check_package)

        self.button_apk_list.clicked.connect(self.check_list)
        self.button_next.clicked.connect(self.check_next)
        self.button_last.clicked.connect(self.check_last)

        self.button_install.clicked.connect(self.install_apps)
        self.button_open.clicked.connect(self.open_apps)
        self.button_uninstall.clicked.connect(self.uninstall_apps)

        self.button_location.clicked.connect(self.browse_file)
        self.button_location_o.clicked.connect(self.open_file)

        self.button_apk.clicked.connect(self.browse_apk)
        self.button_apk_o.clicked.connect(self.open_apk)

        self.button_save.clicked.connect(self.check_package)
        self.button_save.clicked.connect(self.save_gui)

        self.button_tag_phone.clicked.connect(lambda: self.tag_login('phone'))
        self.button_tag_tv.clicked.connect(lambda: self.tag_login('tv'))

        self.button_tag_layout.clicked.connect(self.tag_layout)

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

    def check_list(self):
        global apk_list
        global apk_index
        apk_dir = self.edit_apk_result.text()
        print(apk_dir)
        index = 0
        for root, dirs, files in os.walk(apk_dir):
            apk_list = dirs
            index = len(dirs)
            print(dirs)
            break
        msg = str(index) + ' paired apks are found.'
        print(msg)
        self.label_apk_list.setText(str(msg))
        # QMessageBox.information(self, 'Complete', index + ' paired apk are found!')

    def check_next(self):
        global apk_list
        global apk_index
        if apk_index < len(apk_list) - 1:
            apk_index += 1
            self.label_package.setText(str(apk_list[apk_index]))

    def check_last(self):
        global apk_list
        global apk_index
        if apk_index > 0:
            apk_index -= 1
            self.label_package.setText(str(apk_list[apk_index]))

    def install_apps(self):
        em_1 = self.combobox_em_1.currentText()
        print(em_1)
        em_2 = self.combobox_em_2.currentText()
        print(em_2)
        apk_path_mobile = self.edit_apk_result.text() + '\\' + self.label_package.text() + "\\mobile\\" + self.label_package.text()+ ".apk"
        apk_path_tv = self.edit_apk_result.text() + '\\' + self.label_package.text() + "\\tv\\" + self.label_package.text()+ ".apk"
        print(apk_path_mobile)
        print(apk_path_tv)
        cmd_list = []
        if em_1 == 'phone':
            cmd_list.append('adb -s ' + dev[0] + ' install -r ' + apk_path_mobile)
            cmd_list.append('adb -s ' + dev[1] + ' install -r ' + apk_path_tv)
        else:
            cmd_list.append('adb -s ' + dev[0] + ' install -r ' + apk_path_tv)
            cmd_list.append('adb -s ' + dev[1] + ' install -r ' + apk_path_mobile)
        for cmd in cmd_list:
            r = str(subprocess.check_output(cmd, shell=True))
        QMessageBox.information(self, 'Complete', 'Installed')

    def open_apps(self):
        package_name_temp = self.label_package.text()
        cmd_list = ['adb -s ' + dev[0] + ' shell monkey -p ' + package_name_temp + ' -c android.intent.category.LAUNCHER 1',
                    'adb -s ' + dev[1] + ' shell monkey -p ' + package_name_temp + ' -c android.intent.category.LAUNCHER 1']
        print(cmd_list)
        for cmd in cmd_list:
            r = str(subprocess.check_output(cmd, shell=True))

    def uninstall_apps(self):
        package_name_temp = self.label_package.text()
        cmd_list = ['adb -s ' + dev[0] + ' uninstall ' + package_name_temp,
                    'adb -s ' + dev[1] + ' uninstall ' + package_name_temp]
        for cmd in cmd_list:
            r = str(subprocess.check_output(cmd, shell=True))
        QMessageBox.information(self, 'Complete', 'Uninstalled')

    def check_package(self):
        cmd_list = []
        global dev
        if len(dev) > 0:
            cmd_list.append('adb -s ' + dev[0] + ' shell dumpsys window windows | find "mCurrentFocus"')
            print(cmd_list[0])
            cmd_list.append('adb -s ' + dev[1] + ' shell dumpsys window windows | find "mCurrentFocus"')
            print(cmd_list[1])

        global package_name
        global activity_name

        package_name.clear()
        activity_name.clear()

        index = 0
        for cmd in cmd_list:
            r = str(subprocess.check_output(cmd, shell=True))
            print(r)
            package_details = r.split(" ")[-1].split("/")
            package_name.append(package_details[0])
            # activity_name.append(package_details[-1][:-6].split(".")[-1]) #short activity name
            activity_name.append(package_details[-1][:-6]) # full activity name
            if index == 0:
                self.edit_package_1_result.setText(str(package_name[0]))
                self.edit_activity_1_result.setText(str(activity_name[0]))
            elif index == 1:
                self.edit_package_2_result.setText(str(package_name[1]))
                self.edit_activity_2_result.setText(str(activity_name[1]))
            index += 1

    def browse_file(self):
        # global save_dir
        # https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog
        save_dir = QDir.toNativeSeparators(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        print(save_dir)
        self.edit_location_result.setText(save_dir)

    def open_file(self):
        # print(save_dir)
        save_dir = self.edit_location_result.text()
        os.startfile(save_dir)

    def browse_apk(self):
        # global save_dir
        # https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog
        save_dir = QDir.toNativeSeparators(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        print(save_dir)
        self.edit_apk_result.setText(save_dir)

    def open_apk(self):
        # print(save_dir)
        save_dir = self.edit_apk_result.text()
        os.startfile(save_dir)

    def save_gui(self):

        global save_file
        # global package_name
        package_name_1 = self.edit_package_1_result.text()
        package_name_2 = self.edit_package_2_result.text()
        activity_name_1 = self.edit_activity_1_result.text()
        activity_name_2 = self.edit_activity_2_result.text()

        save_file = self.edit_location_result.text() + "\\" + package_name_1
        if package_name_1 != package_name_2:
            save_file = save_file + "_" + package_name_2

        # https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
        Path(save_file).mkdir(parents=True, exist_ok=True)

        # check the existing folder
        # https://stackoverflow.com/questions/29769181/count-the-number-of-folders-in-a-directory-and-subdirectories
        folders = 0
        for root, dirs, files in os.walk(save_file):
            folders += len(dirs)
        print(folders)
        save_file = save_file + "\\" + str(folders+1)
        print(save_file)
        Path(save_file).mkdir(parents=True, exist_ok=True)

        cmd = []
        # if len(dev) == 1:
        #     cmd_1 = 'adb exec-out screencap -p > ' + save_file + '\\screen_1_' + package_name_1 + '.png'
        #     cmd_2 = 'adb exec-out uiautomator dump /dev/tty > ' + save_file + '\\screen_1_' + package_name_1 + '.xml'
        #     cmd.extend([cmd_1, cmd_2])
        if len(dev) == 2:
            cmd_0_0 = "adb -s " + dev[0]
            cmd_0_1 = "adb -s " + dev[1]
            cmd_1 = cmd_0_0 + ' exec-out screencap -p > ' + save_file + '\\screen_1_' + package_name_1 + '_' + activity_name_1 + '.png'
            cmd_2 = cmd_0_0 + ' exec-out uiautomator dump /dev/tty > ' + save_file + '\\screen_1_' + package_name_1 + '_' + activity_name_1 + '.xml'
            cmd_3 = cmd_0_1 + ' exec-out screencap -p > ' + save_file + '\\screen_2_' + package_name_2 + '_' + activity_name_2 +  '.png'
            cmd_4 = cmd_0_1 + ' exec-out uiautomator dump /dev/tty > ' + save_file + '\\screen_2_' + package_name_2 + '_' + activity_name_2 + '.xml'
            cmd.extend([cmd_1, cmd_2, cmd_3, cmd_4])

        print(cmd)

        # run the command.
        for cmd_e in cmd:
            subprocess.check_output(cmd_e, shell=True)

        # show success dialog
        QMessageBox.information(self, 'Complete', 'The GUI labelling completed!')

    def tag_login(self, device):
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

    def tag_layout(self):
        global save_file
        # global package_name
        package_name_1 = self.label_package.text()
        save_file = self.edit_location_result.text() + "\\" + package_name_1
        # https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
        Path(save_file).mkdir(parents=True, exist_ok=True)
        f = open(save_file + '\\layout_issue_' + package_name_1 + '.txt', 'w')
        f.write('The paired apps have identical layout.')
        f.close()

        # show success dialog
        QMessageBox.information(self, 'Complete', 'The layout issue is tagged!')


app = QApplication(sys.argv)
dialog = Labeller()
dialog.show()
app.exec()
