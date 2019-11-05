from abc import abstractclassmethod,ABC
class TouchScreenlaptop(ABC):
  
    @abstractclassmethod
    def scroll(self):
        pass
    
    def click(self):
        pass
       
class hp(TouchScreenlaptop):
    def scroll(self):
        print("scroll in hp")
        
class dell(TouchScreenlaptop):
    def scroll(self):
        print("scroll in dell")
        
class hpNotebook(hp):
    def click(self):
        print("click on hpNotebook")
    
class dellNotebook(dell):
    def click(self):
        print("Click on dellNotebook")
        
hpn=hpNotebook()
print(hpn.scroll())
print(hpn.click())

de=dellNotebook()
print(de.scroll())
print(de.click())













