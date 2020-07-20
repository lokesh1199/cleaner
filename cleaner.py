import os, shutil
from pathlib import PosixPath
from extensions import combined

class MyPath(PosixPath):
	def __add__(self, other):
		return MyPath(str(self) +'/' + other)


def createDir(dirName):
	os.mkdir(dirName)

def finder():
	'''
	This find the files in the current working
	directory
	'''
	cwd = MyPath.cwd()
	files = []
	for i in os.listdir():
		i = cwd + i
		if not i.is_dir():
			files.append(i)
	return files

def mover(home, dest):
	if not dest.exists():		# If folder doesn't exists
		createDir(dest)			# Creates the folder

	shutil.move(str(home), str(dest))	# moves the file to the folder

def checkExt(file):
	'''
	This checks if given file has extension
	is in the extensions.py
	'''
	ext = file.suffix[1:]		# Removes the '.' 

	for category in combined:	
		if ext in combined[category]:
			return category

def cleaner():
	files = finder()

	for file in files:
		ext = checkExt(file)
		if ext:					# if not None
			mover(file, MyPath.cwd() + ext)
		else:
			print(file, 'is not in the extensions')

if __name__ == '__main__':
	cleaner()



