from sys import argv

script,filename = argv

def printitoff(ptr):
	print(ptr.read())


def rewinditoff(ptr):
	ptr.seek(0)


def printspecific(line,ptr):
	print(line,ptr.readline())


print(f"file that has been entered:> {filename}")
print("lets print the file:")
ptr = open(filename,'r')
print(ptr)
printitoff(ptr)
print("lets rewind")
rewinditoff(ptr)
print("lets print the specific line of file:")
line = input("enter specific number of file")
printspecific(line,ptr)

