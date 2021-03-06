class Renault:
    
    def __init__(self,company,model,year):
        self.company = company
        self.model = model
        self.year = year
    def start(self):
        print("starting the engine")
    def stop(self):
        print("Stopping the engine")
    
        
class threeseries(Renault):
    
    def __init__(self,cruiceControlEnabled,company,model,year):
        super().__init__(company,model,year)  #using super to invoke superclass constructor
        self.cruiceControlEnabled = cruiceControlEnabled
    def display(self):
        print("this is three series car")
        
    def start(self):
        super().start()  #also used for invoking superclass functions first
        print("this statement is in override method")
    
class fiveseries(Renault):
    
    def __init__(self,parkingAassistEnabled,company,model,year):
        super().__init__(company,model,year)   #using super to invoke superclass constructor
        self.parkingAassistEnabled = parkingAassistEnabled
    def stop(self):
        super().stop()
        print("this statement is in override method")
    def dis(self):
        print("this is five series car")
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

"""---------------------------------------------------------------"""
#to inherit the method
three.start()

five.stop()
"""----------------------------------------------------------------"""
#subclass can define their own functions
three.display()
five.dis()

    