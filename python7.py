"""
#
# Part : Python Class and Object
#
"""
#build class
class Myclass:
    x = 5

#Call class
object1 = Myclass()
print("object1 =", object1.x)
object2 = Myclass()
print("object2 =", object2.x)

class SpyXFamily:
    def __init__(self, name_f, age_f):
        self.name = name_f
        self.age = age_f
        
    def __str__(self):
        return f"{self.name} - {self.age}"
    
    def sayhi(self, last_name = "forger"):
        print(f"Hey bro what'sup {self.name} {last_name}")
        
        
p1 = SpyXFamily("Anya", 8)
print(p1.name, p1.age)
print(p1)
p1.sayhi()

p2 = SpyXFamily("Damian", 8)
print(p2.name, p2.age)
print(p2)
p2.sayhi("Desmond")

class Car:
    def __init__(self, body_color, engine_size):
        self.wheels = 4
        self.window = 4
        self.window_front = 1
        self.window_back = 1 
        self.body_color = body_color
        self.engine_size = engine_size
        
    def push_window_botton(self):
        #do something
        pass 
    
    def pop_window_buttoon(self):
        #do something
        pass 
    
    def calSpeed(self):
        #speed = self.engine_size * 1000
        #return speed
        return self.engine_size * 1000
    
    def turnOnFrontLight(self, status = "off"):
        if status == "on":
            #do something
            pass
        else:    
            #do something
            pass