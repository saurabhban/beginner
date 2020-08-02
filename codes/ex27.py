from sys import argv


def sortfile(file1):

	target = open(file1,'r')
	target1 =open(file1,'a')
	for line in target:
		line = ''.join(sorted(line)) 
		print(line)
		target1.write('\n')
		target1.write(line)
	target.close()
	target1.close()
		
def splititup(stringname):
	name=stringname.split('_')
	return name




script,file1,file2 =argv
print(f"source file entered {file1} and destination file entered {file2}")
sortfile (file1)
stringname=input("enter the string to split")
name=splititup(stringname)
print(name)


