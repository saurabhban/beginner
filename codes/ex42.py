from os import walk, sep
from sys import argv
import os
from os.path import basename, isdir

#def tree(start_path,print_files=False):

#	for root,subdirs,files in walk(start_path):
#		level = root.replace(start_path, '').count(sep)
#		indent = '  |' * (level-1) + '  +- '
#		print "%s%s/" % (indent, basename(root))
#		subindent = '  |' * (level) + '  +- '
##		if print_files:
#			for f in files:
#				print (f)
				

def isbinod(items):
	with open (items,'r') as f:
		filecontent = f.read()
		if "binod" in filecontent.lower():
			return lower
		else:
			return false



def search(strings,path):
	dir_contents = os.listdir(path)
	print(dir_contents)
	for items in dir_contents:
		if items.endswith('txt'):
			print("detecting binod in",items)
			t=isbinod(items)
			if t == true:
				print ("binod found in", items)

				


#def usage():
#	return '''Usage: %s [-h] [-f] [PATH]
#	Print tree structure.
#	Options:
#	-h, --help	Print help info
#	-f			Print files as well as directories
#	PATH		Path to process
#	-binod agent binod search''' % basename(argv[0])


def main():

	print("hello world")

	path =input("enter the path")
	if ('-h' or '--help') in argv:
		print()
		#print usage()
	elif len(argv) == 1:
		tree(path)

	elif len(argv) == 2 and argv[1] == '-f':
		tree(path,True)

	elif len(argv) == 2 and argv[1] == "binod":
         search("binod",path)





if __name__ == '__main__':
	main()





