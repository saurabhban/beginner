from sys import argv
from os.path import exists

script, from_file, to_file = argv
print (f"Copying from {from_file} to {to_file}")
ptr1 = open(from_file)
raw_data1 = ptr1.read()
lenght=len(raw_data1)
print(f"input data in {lenght} long")
print(f"does destination file {to_file} exists ?")
print(exists(to_file)) # used exists function from os.path
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
ptr2 = open(to_file,'+w') #open the second file in write mode after creating it
ptr2.write(raw_data1) #write the data we read into second file
ptr1.close() #close the file pointer for first file
ptr2.close() #close the file pointer of 2nd file



