class Patient:
    def setId(self,id):
        self.__id = id
        
    def getId(self):
        return self.__id
    
    def setName(self,name):
        self.__name=name
        
    def getname(self):
        return self.__name
    
    def setssn(self,ssn):
        self.__ssn = ssn
        
    def getssn(self):
        return self.__ssn
    
p = Patient()
p.setName("Pradeep")
p.setId(111)
p.setssn("hosp123")
print("Patient Id is:",p.getId())
print("patient name is",p.getname())
print("patient ssn is:",p.getssn())
        
    