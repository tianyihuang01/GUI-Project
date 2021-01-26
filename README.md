# GUI-Project

Updated on 26/01/2021

## GUI Labbeller

### About

A desktop app to label the GUIs from two Android emulators.

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

### How to use

1. Make sure you have:
    - At least two .apk files of the apps you want to analyze.
    - Exact two emulators connected to your host machine via adb.

2. Emulator configuations:
    - Turn on the **developer options** > **USB debugging**
    - Install and run two apk files to the two emulators respectively

3. Run `GUILabeller.py`
    1. Click **Check Emulators** button. 
        - Make sure the names of two emulators are displayed.
    2. Check and change the GUI in the two emulators, Stop at the GUI to label.

    3. Click **Check Packages** button.
        - Name sure package names and activity name are correctly displayed.
    4. (Optional) Click **Save Location** button to specify the path to save GUI files.
        - A default path has been displayed.
    5. Click ***Get n Save*** button to save the screenshot and description files of GUIs.
        - When the complete message pops up, the GUI files is successfully saved.
        - the default path: [save location]/[package name]/[foler]/......
    6. Repeat step 2 and 5 to label to save more GUI files.
        - If there are some login issues, record the issue by clicking ***phone*** and/or ***tv*** button to specify the app. 
         - When the complete message pops up, the issued is successfully recorded.
    

