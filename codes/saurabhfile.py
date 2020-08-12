import os
 
def findtext(dir,phrase):

	for file in os.listdir(dir):
		path = dir + "/" + file
		if os.path.isdir(path):
			findtext(path, phrase)
		else:
			f = open(path)
			ptr = f.read()
			print(ptr)
			if "saurabh" in ptr:
				print("binod found")
			
 
findtext("/Users/saurbane/miscellaneous/cisco", "Binod")