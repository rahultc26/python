from abc import abstractclassmethod,ABC
class Renault(ABC):
    
    def __init__(self,company,model,year):
        self.company = company
        self.model = model
        self.year = year
    def start(self):
        print("starting the engine")
    def stop(self):
        print("Stopping the engine")
    
    @abstractclassmethod           #abstract method
    def drive(self):
        pass
        
        
class threeseries(Renault):
    
    def __init__(self,cruiceControlEnabled,company,model,year):
        Renault.__init__(self,company,model,year)
        self.cruiceControlEnabled = cruiceControlEnabled
    def display(self):
        print("this is three series car")
    
    
    def drive(self):
        print("Threeseries is driven")   #abstract method
    
class fiveseries(Renault):
    
    def __init__(self,parkingAassistEnabled,company,model,year):
        Renault.__init__(self,company,model,year)
        self.parkingAassistEnabled = parkingAassistEnabled
    
    def dis(self):
        print("this is five series car")
        
    def drive(self):
        print("five series is driven")   #abstract method
        
    
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
three.stop()

"""----------------------------------------------------------------"""
#subclass can define their own functions
three.display()
five.dis()






    