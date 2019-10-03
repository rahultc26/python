class Course:
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings
        
c1 = Course("Artificial Intelligence",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)


#Using another object
c2 = Course("Python",[1,2,3,4,5])
print(c2.name)
print(c2.ratings)