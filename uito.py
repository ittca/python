import os
from os import path

# small program to convert ui files to .py files of the qt5 Design once the "view python code" option doesn't work
# paste this file in a python directory that is a path enviroment
# one like "C:\Users\"your_user"\AppData\Local\Programs\Python\Python38-32\Scripts\"
# then to use just do a "cd ui_file_directory" and call "uipy.py"
# the file name input should not have extension.
# for example "amazing.ui" should be inputed like "amazing"

file = input("ui file name without extension >  ")
if (path.isfile(f'{file}.ui')):
    os.system(f'python -m PyQt5.uic.pyuic -x {file}.ui -o ui_{file}.py')
    print(f'\n ui_{file}.py has been created with success!')
else:
    print(f'\nThe {file}.ui is not present in this directory')
