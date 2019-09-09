s0="awesome "
s="my name is rahul " 
s2='i am learning python'

print(s.find("rah"))  #find function

print(s2.find("lea"),len(s2))  #also including length of the particular string

print(s0.count("e"))  #number of counts o/p:2
print(s.count("a"))   #number of counts o/p:2

#to replace the string characters
print(s.replace("my", "the"))  # the is replaced by my
print(s)                       #o/p = the name is rahul

#converting string into uppercase,lowercase and title case
print(s0.upper())
print(s0.lower())
print(s.title())