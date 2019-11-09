try:
    f = open("myfile","w")
    a,b = [int(x) for x in input("enter the two numbers\n").split()]
    c = a/b;
    print("division ",c)
    f.write("writing %d into file" %c)
except ZeroDivisionError:
    print("ZeroDivision not allowed")
    print("this is after exception")
    
else:
    print("This is else statement")
finally:
    f.close()
    print("file closed")