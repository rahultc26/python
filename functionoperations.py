"""#using of return
def calc(a,b):
    x=(a+b)
    y=(a-b)
    z=(a*b)
    w=(a/b)
    return w,x,z,y
print(calc(1000,50))


#function in function
def dis(name):
    def mess():
        return "Hello "
    res = mess()+name
    return res
print(dis("rahul"))


#returning the function
def diss():
    def messege():
        return "Rahul"
    return messege
f=dis()
print(f()) 

#passing any type to functions
def list(lst):
    for i in lst:
        print(i)
list([10,20,30,40,50]) """

#passing set to function
def set(s):
    for i in s:print(i)
set({1,2,3,4})


