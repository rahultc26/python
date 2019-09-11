#creating lists
lst=[1,34,56,'india',55.5]
s=[1,2,3]

#indexing
print(lst[1]) #prints the value in lst of index 1
print(lst[3]) #prints the value in lst of index 3 that is 'india'

#slicing in list
print(lst[0:3]) #prints the lements from list from index 0 to 3 but not prints the 3rd index value

#repetition in lists
print(s*2) #prints s list two times
print(lst*2) #prints 'lst' list two times


#finding length
print(len(s)) #display the length of the list 's'
print(len(lst)) #display the length of the list 'lst'

#adding the values to the list
lst.append('rahul')  #'rahul is added at the last index of the list'
print(lst)
lst.append(2)        #again '2' is added at last of the list
print(lst)    

#removing the element from the list
lst.remove(56)   #it removes 56 from list 'lst'
lst.remove('rahul')  #also it removes rahul from list 'lst'
#NOTE: The value your giving inside the bracket is must match with list which you are created before

#deleting value by specifying the index value
del(lst[1])   #delete the value in index '1' from the list name called 'lst' 
print(lst)

#NOTE: 'del' is inbuilt function in python not on the list

#---------------------------------------------------------------------------------------------------#

#Some more operations on Lists
l=[1,2,3,4]

#To clear the list
l.clear()  #completely clears the list
print(l)  # so the o/p=[]

#To find the maximum element in the list
#lets take
lt=[10,44,34.34,33,88]
print(max(lt))   #max is used to find and o/p=88

#To insert elements in the list
lt.insert(2, 100)  #where '2' is index and '100' is inserted object
print(lt)               #at the index 2 100 will be inserted 

#sorting in list
lt.sort()            #Sorts the list in ascending order
print(lt)  

#To sort in descending order
lt.sort(reverse=True) 
print(lt)


