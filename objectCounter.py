class objectcount:
    numofob = 0
    
    def __init__(self):
        objectcount.numofob+=1   #whenever init function is invoked numofob is incrementedby one
        
    @staticmethod
    def display():
        print("Number of objects created are :",objectcount.numofob)
        
o1 = objectcount()
o2 = objectcount()
o3 = objectcount()

objectcount.display()   

#output : Number of objects created are : 3
    