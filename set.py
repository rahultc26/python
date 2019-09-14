#Creating set

s={10,20,30,'rc',50}
print(s)

#we can't add same elements it'll not take
s={10,11,13,10,12,11}
print(s)  #o/p={10, 11, 12, 13}

#Note:we can't do indexing slicing and repetition in set

#we can do update set by adding elements
s={10,20,55,99}
s.update([60,70]) 
print(s)        #o/p={99, 70, 10, 20, 55, 60} there is no specific order in set therefore elements are added without order


#we can do removing
s={10,20,30}
s.remove(20)  #'20' will be removed
print(s)   #o/p={10, 30}

