from sys import argv
import re

def findpattern(file1,search):
	count =0
	with open (file1,'r') as ptr:
		for line in ptr:
			line=line.lower()
			pattern=re.search(search,line)
			if(pattern):
				count=count+1

		print(f"number of places found{count}")

    

    

    
    




file1 = argv[1]
search = input("enter the string to search")
print(search)
search=search.lower()
search=search.lstrip()
findpattern(file1,search)