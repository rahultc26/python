#tuple
#creating Tuple
tup=(10,20,30,'rc')
print(tup)

#eg
tup=(20,)  #if your creating tuple for one value you 
 #must put comma after value otherwise it will consider as integer type 
print(tup) 

#eg
tup=(40)
print(tup)  #it displays int value 40 now

#finding 
print(type(tup))  #displays class int;

tup=(20,)
print(type(tup))  #displays class tuple

#indexing 
tup=(10,20,50,65,'rc')
print(tup[2])  #o/p=50

#repetition
print(tup*2)  #displays contents of tuple twice

#Find count values
print(tup.count(10))  #o/p=1; because there is only one '10'

#finding index value of value on tuple
print(tup.index("rc"))  #index value within double quotes;


#conversion from list to tuple
lst=[10,20,'rc']
print(type(lst))
lst=tuple(tup)
print(type(tup)) #o/p= class lst
                 #     class tuple

 print(tup)   #o/p=(10,20,50,65,'rc')
