def gen(a,b):
    while a<b:
        yield a
        a+=1
        
rs = gen(10,20)
for i in rs:print(i)

"""----------------------------------------------------"""

def gen2(a,b):
    while a<b:
        yield a*b
        a+=1
        
rs = gen2(10,20)
for i in rs:print(i)


def gen3(a,b):
    while a<b:
        yield a/b
        a+=1
        
rs = gen3(10,20)
for i in rs:print(i)

"""------------------------------------------------------"""
def gen4(a,b):
    while a<b:
        yield a-b
        a+=1
        
rs = gen4(20,10)
for i in rs:print(i)