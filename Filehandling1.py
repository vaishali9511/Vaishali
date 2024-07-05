#Filehandling
#2.isFile()
import os

"""
b=os.path.isfile("second1.txt")
print(b)
"""
print(os.stat("second.txt"))

"""
if  os.path.isfile("second.txt"):
   f=open("second.txt","r")
   data=f.read()
   print(data)
   f.close()
else:
    print("There is no such file")
"""



"""
1.r+ w+ with seek and tell
****************************


f=open("second.txt","w+")
f.write("Python is easy")
print(f.tell())
f.seek(0)
data=f.read()
print(data)
f.close()
"""


"""
f=open("second.txt","r+")
f.write("Hello")
print(f.tell())
f.seek(0)
data=f.read()
print(data)
f.close()
"""

#5.tell(), fseek()
"""
f=open("second.txt","r")
print(f.tell())
print(f.read(7))
print(f.tell())
f.seek(2)
print(f.tell())
print(f.read())
f.seek(23)
print(f.tell())
print(f.read())
"""

#f.close()




#4.a,r+,w+,a+
"""
with open("second.txt","a+") as f:
    f.write("\nHtml are tags ")
    data = f.read()
    print(data)
"""



#3.with
"""
with open("second.txt","w") as f:
    f.write("Django is framework of python")
    print("Is file closed:",f.closed)

print("...Is file closed:",f.closed)
"""

#2.read

"""
f=open("second.txt","r")
data=f.readlines()
print(type(data))
print(data)
for l in data:
    print(l)
"""

"""data=f.readline()
print(data)
"""
"""
data=f.read(9)
print(data)
"""


"""
data=f.read()
print(type(data))
print(data)
"""
#f.write("Hello")
#f.close()



#1.write

"""
f=open("second.txt","w")
f.writelines(["Python is easy\n","Core Javaaaa is lengthy\n","FrontEndee\n"])
f.close()
"""

"""
l=["Python\n","Core Java\n","FrontEnd\n"]
f.writelines(l)
f.close()
"""

"""
f=open("first.txt","w")
f.write("My name is Vaishali Shete\n")
f.write("I am a Python Trainer")
f.close()
"""





"""
f=open("first.txt","w")
print("filename:",f.name)
print("mode of file:",f.mode)
print("Is it readable:",f.readable())
print("Is it writable:",f.writable())
print("Is it closed:",f.closed)
f.close()
print("Is it closed:",f.closed)
"""
