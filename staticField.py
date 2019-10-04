class Student:
    branch = "CSE"
    
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
        
s1 = Student("rahul",70)
print(s1.name)
print(s1.usn)
print(Student.branch)

print(Student.branch)  #we can access the field without using object