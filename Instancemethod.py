'''Definition : An instance, in object-oriented programming (OOP), 
is a specific realization of any object.
An object may be varied in a number of ways. 
Each realized variation of that object is an instance.'''

class Course:
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings
        
    def average(self):
        numofratings = len(self.ratings)
        average = sum(self.ratings)/numofratings
        print("Average rating of ",self.name," course is",average,"Out of 5")
        
c1 = Course("Artificial Intelligence",[4,5,5,5,5])
print(c1.name)
print(c1.ratings)
c1.average()

#using another object
c2 = Course("Python",[3,4,5,4,5])
print(c2.name)
print(c2.ratings)
c2.average()