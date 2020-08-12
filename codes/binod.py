import os

def showfiles(path):
	for folders , dirs , file in os.walk(path):
		for files in file:
			if files.endswith('.txt'):
				print(files)

def spammer(path):
	for folder ,dirs, file in os.walk(path):
		for files in file:
			if files.endswith('txt'):
				fullpath = open(os.path.join(folder,files),'r')
				lines = fullpath.read()
				lines = lines.lower()
				if 'binod' in lines:
					print(os.path.join(folder,files))




path = input ("enter the path to check")
print("*"*30)

print("lets see how many folders and file present in path")
showfiles(path)

print("invoking Bindod Spam Detector :D")
print("*"*30)

spammer(path)

