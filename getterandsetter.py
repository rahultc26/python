class student:
    def setusn(self,usn):
        self.usn = usn
        
    def getusn(self):
        return self.usn
    
    def setname(self,name):
        self.name = name
        
    def getname(self):
        return self.name
    
s = student()
s.setusn('cs070')
s.setname("Rahultc")
print("Student usn:",s.getusn())
print("Student name",s.getname())