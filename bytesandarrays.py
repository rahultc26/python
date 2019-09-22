#lets take one list

lst=[10,22,30,45,234]   #max value we can take is 235
print(type(lst))   #class list

#converting lst int bytes
b=bytes(lst)
print(type(b))  #coverted to type bytes

b[2]=12    #Note:we can not modify the bytes but we can modify using 'byte arrays'

#converting lst to bytearray
b1=bytearray(lst)
print(type(b1))  #converted to bytesarrays

#modifying
b1[2]=111
   #there is no issues in o/p
   
 #example
 b1[3]=121  #again there is no issues in o/p
