
s=input()  #Taking input from user
print(s)

t=input("enter your name\n")
print("entered name is",t)

#Typecasting

i=int(input("Enter integer value:\n"))
print("Entered value is: ",i)
print(type(i))   #class int 

"""Gving multiple inputs
For multiple inputs we have to use looping"""

lst=[x for x in input("enter 3 values seperated by space").split()] ##i/p = 1 2 3
print(lst)  #o/p=['1', '2', '3']

#coverting ino int
lst=[int(x) for x in input("enter 3 int values seperated by commas\n").split(',')] #i/p = 1,2,3
print(lst)   #o/p=[1, 2, 3]

#converting into float
lst=[float(x) for x in input("enter 3 floaty values\n").split(",")] #i/p = 10.5,2.2,3.10
print(lst)   #o/p = [10.5, 2.2, 3.1]

#NOTE : split function uses delimeter space by default
