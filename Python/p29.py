from keyword import kwlist
import os, stat
import pickle

#10. Write a Python script to extract book data from a 
# bookfile using pickle. Also print extracted book data.
#9. Write a Python script to store book data in a file. 
# Book data is in the form of a dictionary in which 
# book name is the key and price is its value. Use pickle 
# to store data into a file (say bookfile)
book_data={'C':200,'C++':500,'Python':600,'Java':820}
fd=open('bookfile','wb')
pickle.dump(book_data,fd)
fd.close()

fd=open('bookfile','rb')
data=pickle.load(fd)
for key in data:
    print(key,data[key],sep='\t')
fd.close()

#8. Write a Python script to create a copy of a file.
try:
    fd1=open("test1.py",'r')
    fd2=open("Copy of test.py",'w')
    lines=fd1.readlines()
    fd2.writelines(lines)
    fd1.close()
    fd2.close()
except FileNotFoundError:
    print("FileNotFoundError")

#7. Write a Python script to count the number of Python keywords occurring
#  in a python source file.
fd=open("p25.py",'r')
lines=fd.readlines()
fd.close()
s=set()
for e in lines:
    for i in e.split(None):
        for k in kwlist:
            if k==i:
                s.add(k)

print("Keyword used",s)

#6. Write a Python script to search whether a particular city is there in the 
# file ‘cities.txt’ or not
#5. Write a Python script to append list of city names in a file ‘cities.txt’
#4. Write a Python script to store a list of city names in a file ‘cities.txt’
fd=open("cities.txt",'w+')
city_list=['delhi','mumbai','italy','surat']
for e in city_list:
    fd.writelines(e)
    fd.write('\n')
fd.close()

fd=open("cities.txt",'a')
city_list=['hubli','hyd','blore','milan']
for e in city_list:
    fd.write(e)
    fd.write('\n')
fd.close()

fd=open("cities.txt",'r')
text=fd.read()
print(text)
fd.close()

def search(city):
    with open("cities.txt",'r') as fd:
        line=fd.read()
        if line.lower().find(city) != -1:
            fd.close()
            return True
    fd.close()
    return False

print("City found") if search('mumbar') else print("City not found")

#3. Write a Python script to read the above created file ‘myfile.txt’ and display 
# content on the console.
#2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
fd=open("myfile.txt",'w+')
fd.write(input("Enter data to write to file: "))
fd.close()
fd=open("myfile.txt",'r')
text=fd.read()
print(text)
fd.close()

#1. Write a Python script to print the following status of a file:
# a. Whether a file is read only
# b. Whether a file is closed or not
# c. Which file opening mode is used
# d. Name of the file
file_exists=os.path.exists("/Users/amarkamat/Downloads/Amar/Python/Assignment/pythonPrograms/demo.py")
if file_exists:
    status=os.stat("/Users/amarkamat/Downloads/Amar/Python/Assignment/pythonPrograms/demo.py")
    print("File is Read-Only") if int(status.st_mode)&(stat.S_IREAD|stat.S_IWRITE|stat.S_IEXEC) == stat.S_IREAD else print("File is not Readonly")

f=open("/Users/amarkamat/Downloads/Amar/Python/Assignment/pythonPrograms/demo.py",'r+')
print("File is Read-Only") if f.mode=='r' else print("File is not Readonly")
print("File is closed") if f.closed else print("File is open")
print("File mode used", f.mode)
print("File name is",f.name)