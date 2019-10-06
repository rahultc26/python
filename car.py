class Renault:
    
    def __init__(self,company,model,year):
        self.company = company
        self.model = model
        self.year = year
        
class threeseries(Renault):
    
    def __init__(self,cruiceControlEnabled,company,model,year):
        Renault.__init__(self,company,model,year)
        self.cruiceControlEnabled = cruiceControlEnabled
    
class fiveseries(Renault):
    
    def __init__(self,parkingAassistEnabled,company,model,year):
        Renault.__init__(self,company,model,year)
        self.parkingAassistEnabled = parkingAassistEnabled
    
    
three = threeseries(True,"Duster","1511","2015")
print(three.cruiceControlEnabled)
print(three.company)
print(three.model)
print(three.year)
print("")
five = fiveseries(True,"kwid","1523","2017")
print(five.parkingAassistEnabled)
print(five.company)
print(five.model)
print(five.year)


    