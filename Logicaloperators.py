""" Logical operators
    and
    or
    not """

x,y=10,20

print((x==10 and y==20))  #returns true because both statements are true

print((x==11 and y==20))  #false one statement is false 

print((x==11 or y==20))    #true in or operator if one statment is true the whole expression is true

print(not(x==10 and y==20))  #using not the true statment becomes false

print(not(x==999))   #returns true