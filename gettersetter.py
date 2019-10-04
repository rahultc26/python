class Programmer:
    def setName(self,Name):
        self.name = Name
        
    def getname(self):
        return self.name
        
    def setSalary(self,sal):
        self.Salary = sal
        
    def getSalary(self):
        return self.Salary
    
    def setTechs(self,tech):
        self.Techs = tech
        
    def getTechs(self):
        return self.Techs
    
p1 = Programmer()
p1.setName("Rahul")
p1.setSalary(50000)
p1.setTechs(["Java","Python","Mysql"])

print("Programmer details are..")
print("Name",p1.getname())
print("Salary",p1.getSalary())
print("Skills",p1.getTechs())