class flight:
    def __init__(self,engine):
        self.engine=engine;
        
    def startengine(self):
        self.engine.start();
        
        
class Airbusengine:
    def start(self):
        print("Airbus engine starting")
        
class Boingengine:
    def start(self):
        print("Bong engine Satring");
        
class name:       
    def start(self):
        print("hello")
    
    
ae = Airbusengine()
f = flight(ae)
f.startengine()

be = Boingengine()
f1 = flight(be)
f1.startengine()

s = name()
f2 = flight(s)
f2.startengine()