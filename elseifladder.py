maths=int(input("enter the maths marks\n"))

phy=int(input("enter the physics marks\n"))

chem=int(input("enter the chemistry marks\n"))

avg=(maths+phy+chem)/3

if(avg<35):
    print("Student failed in exams")
elif(avg>=35):
    print("Student passed in exams")
if(avg <= 59):
    print("Student Grade is C")
elif(avg<=69):
    print("Student Grade is B")
else:
    print("Student Grade is A")
    

