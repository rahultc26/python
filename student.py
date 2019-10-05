class student:
    def __init__(self):
        self.__id = 70
        self.__name = "rahul"
        
    def display(self):
        print(self.__id)
        print(self.__name)
        
s = student()
s.display()   #another method displayed below

#---------------------------------------------------
"""
print("id:",s._student__id);
print("name:",s._student__name);"""