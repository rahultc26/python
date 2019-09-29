def factorial(n):
    if n==0:
        res=1
    else:
        res=n*factorial(n-1)
    return res
print(factorial(4))