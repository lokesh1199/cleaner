import os
import shutil
from pathlib import Path
from extensions import combined


def createDir(dirName):
    os.mkdir(dirName)


def finder(downPath):
    '''
    This find the files in the current working
    directory
    '''
    cwd = downPath
    files = []
    for i in os.listdir(cwd):
        i = cwd / i
        if not i.is_dir():
            files.append(i)
    return files


def mover(home, dest):
    if not dest.exists():		# If folder doesn't exists
        createDir(dest)			# Creates the folder

    shutil.move(str(home), str(dest))  # moves the file to the folder


def checkExt(file):
    '''
    This checks if given file has extension
    is in the extensions.py
    '''

    for category in combined:
        for extension in combined[category]:
            if str(file).endswith(extension):
                return category


def setup():
    '''
    setup asks default path for cleaning
    if you want to change the path afterwards
    you can change it in 'cleaner.config' file
    '''

    if not (Path.cwd() / 'cleaner.config').is_file():
        downPath = input('Enter Path for cleaning\n(Eg: /home/user/Downloads)')
        if not (Path.cwd() / downPath).is_dir():
            print('Invalid Path')
            exit()

        with open('cleaner.config', 'w') as f:
            f.write(downPath)
    with open('cleaner.config') as f:
        file = f.read()
    return Path(file)


def cleaner(downPath):
    files = finder(downPath)

    for file in files:
        ext = checkExt(file)
        if ext:					# if not None
            mover(file, downPath / ext)
        else:
            print(file, 'is not in the extensions')


if __name__ == '__main__':
    cleaner(setup())
