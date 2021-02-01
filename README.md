# GUI-Project

Updated on 01/02/2021

## GUI Labbeller

### About

A desktop app to label the GUIs from two Android emulators (phone and tv).

### Prerequiste

1. `Python 3.x`
2. `PyQt 5`
    - Instruction： <https://www.riverbankcomputing.com/software/pyqt/download>
    - Reference Guide: <https://www.riverbankcomputing.com/static/Docs/PyQt5/>
3. `Andorid Emulator`
    - the following tools have been tested:
        - Genymotion: <https://www.genymotion.com/fun-zone/>
        - Android Studio (Recommend): <https://developer.android.com/studio>
4. (Optional) `IDE for Python`

### Configuration

1. Make sure you have:
    - At least two .apk files of the apps you want to analyze.
    - Exact two emulators (Android phone and tv) connected to your host machine via adb.

2. Emulator configuations:
    - Turn on the **developer options** > **USB debugging**

### Run `GUILabeller.py`

1. Click **Check Emulators** button. 
    - Make sure the names of two emulators are displayed.
2. Click the drop-down list the specify the phone and tv emulators.
    - Cannot identify them? Click **Check Packages** button to display the package and activity names of two emulators.
3. Click **Apk Location** button to specify the root path of apk files.
    - For each paired apk, the file structure should be:
        - ./[package_name]/mobile/[apk_name].apk
        - ./[package_name]/tv/[apk_name].apk
4. Click **Check Packages** button.
    - If the root path of apk files is correct, it will display the number of pair apks found.

5. Click **Next App** mulitple times to traverse the package names of app, stop at the app to test.
6. Click **Install Apps** button.
    - When the complete message pops up, the apps are successfully installed in  the phone and tv emulator respectively.
7. Click **Launch Apps** button. both the phone app and the tv apps will display in the emulator.

8. (Optional) Click **Save Location** button to specify the path to save GUI files.
    - A default path has been displayed

9. Check and change the GUI in the two emulators, Stop at the GUI to label.

10. Click **Check Packages** button.
    - Name sure package names and activity name are correctly displayed.

11. Click ***Get n Save*** button to save the screenshot and description files of GUIs.
    - When the complete message pops up, the GUI files is successfully saved.
    - the default path: [save location]/[package name]/[foler]/......

12. Repeat step 9-11 to label more GUIs.
    - If there are some login issues, record the issue by clicking ***phone*** and/or ***tv*** button to specify the app. 
    - If the GUI layout of the two apps are exactly same, click **yes** button to record the issue.
        - When the complete message pops up, the issued is successfully recorded.

13. When the test is complete, click **Uninstall Apps** button to uninstall the apps. It will reduce the compatiblity issue when install the second paired apps.

14. Wants to test another paired apps? 
    - return to step 5.
15. Wants to exit? 
    - Click **Close** button.

