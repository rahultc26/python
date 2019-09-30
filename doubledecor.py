def decor(fun):
    def inn():
        result = fun()
        return result*2
    return inn
    
def num():
    return 7

res = decor(num)
print("Double is",res())        #o/p = 14

"""------------------------------------------------------------"""

#Another way
def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decorfun
def number():
    return 7

print("Double is",number())  #o/p = 14


    