a=[1,2,4,5,6]
b=[2,5,1,10]

'''result=[]
for i in a:
    if i in b:
        result.append(i) this is normal'''
        
#Using list comprehensions
result=[i for i in a if i in b]
print(result)
        
        