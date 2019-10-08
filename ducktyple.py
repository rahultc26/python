class duck:
    def talk(self):
        print("duck sounds 'quack quack'")
        
class human:
    def talk(self):
        print("human sounds-Hello!")
        
def calltalk(obj):
    obj.talk()
    
d = duck()
calltalk(d)

h = human()
calltalk(h)
    
