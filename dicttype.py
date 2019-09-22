#Dictionary

#creating a dictionaries

dict={1:"rc",2:"ram",3:"rax"}  #here 1,2,3,are the keys to the values called rc,ram,rax respectively

print(dict)   #o/p {1:"rc",2:"ram",3:"rax"}

#using item methods in dictionaries

print(dict.items())  #displays all values separated by parentheses


#Note: There are several methods you can use with dictionary

#displaying only keys in dictionary
k=dict.keys()
for i in k:print(i)  #o/p = 1 2 3

#displaying only values in dictionary
v=dict.values()
for i in v:
    print(i)  #displays all values one by one
    
#we can also access the value by specifying the key value
print(dict[1])   #o/p = rc

print(dict[2])  #o/p = ram

#deleting the specific value using 'del' method in python
del dict[3]

print(dict)  #o/p = {1: 'rc', 2: 'ram'}

del dict[2]
print(dict)  #o/p = {1: 'rc'}








