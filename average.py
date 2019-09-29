def average(a,b):
    print("Average of",a,"and",b,"is:",(a+b)/2)
average(100,185)  #you can pass any parameters 

#using return
def avg(a,b):
    return (a+b)/2
result = avg(100,185)
print(result)

#another way using return
def avrg(a,b):
    return "average is",(a+b)/2
print(avrg(100,185))
