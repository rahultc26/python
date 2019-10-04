
class Car:
    def __init__(self,company,year):
        self.company = company
        self.year = year
        print("car company is:",self.company)
        print("car purchased",self.year)
        
    class carnumber:
        def __init__(self,num):
            self.number = num
            print("car number is:",self.number) 
        
            
c = Car("Renault-Duster",2015)
n = c.carnumber(2624)




            
            
        
        