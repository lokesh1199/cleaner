import shutil
from pathlib import Path, os

from extensions import extensions


def createDir(dirName):
    os.mkdir(dirName)


def getFiles(downPath):
    '''
    This find the files in the current working
    directory
    '''

    for file in os.listdir(downPath):
        file = downPath / file
        if not file.is_dir():
            yield str(file)


def moveFile(home, dest):
    if not dest.exists():		# If folder doesn't exists
        createDir(dest)			# Creates the folder

    shutil.move(home, dest)  # moves the file to the folder


def checkExtension(file):
    '''
    This checks if given file has extension
    is in the defined extensions
    '''

    extension = file.split('.')[-1]
    return extensions.get(extension, None)


def setup():
    '''
    setup asks default path for cleaning
    if you want to change the path afterwards
    you can change it in 'cleaner.config' file
    '''

    if not (Path.cwd() / 'cleaner.config').is_file():
        downPath = input(
            'Enter Path for cleaning\n(Eg: /home/user/Downloads): ')
        if not (Path.cwd() / downPath).is_dir():
            print('Invalid Path')
            exit()

        with open('cleaner.config', 'w') as f:
            f.write(downPath)
    with open('cleaner.config') as f:
        file = f.read()
    return Path(file)


def cleaner(downPath):
    for file in getFiles(downPath):
        ext = checkExtension(file)
        if ext:					# if not None
            moveFile(file, downPath / ext)
        else:
            print(file, 'is not in the extensions')


if __name__ == '__main__':
    cleaner(setup())
