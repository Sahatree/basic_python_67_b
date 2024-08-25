"""
#
# Part : Python while loop
#
"""

i = 1
while i < 5:
    print("i =", i)
    i+=1 # i = i +1

#i=1
#while i < 5:   
#     print("i =", i)
#     if i == 3:
#        break
#    i+=1 # i = i +1
    
#i=1
#while i < 5:   
#     print("i =", i)
#     if i == 3:
#        continue
#    i+=1 # i = i +1

i=1
while i < 5:   
    print("i =", i)
    i+=1 # i = i +1
else:
    print("Game Over!")
    
"""
#
# Part : Python For loop
#
"""
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print("fruit:", fruit)
    
for fruit in fruits:
    print("fruit:", fruit)
    if fruit == "banana":
        break   
    
for fruit in fruits:
    if fruit == "banana":
        break
    print("fruit:", fruit)   
    
for fruit in fruits:
    if fruit == "banana":
        continue
    print("fruit:", fruit) 
    
for x in range(len(fruits)):
    print("Number", x)
    
for x in range(5):
    print("Number", x)
else:
    print("Game Over!")

adjs = ["red", "blue", "green"]
fruit = ["apple", "banana", "coconut"]
for adj in adjs:
    for fruit in fruits:
        print("friut:" + adj + " " +fruit)
    
"""
#
# Part : Python Function
#
"""
def myFuntion():
    i = 1
    while i <= 5:
        print("Hello World", i)
        i+=1
    
myFuntion()
myFuntion()

# parameter
def myName(name):
    print("My name is " + name)
myName("Anya")
myName("Loid")

def myFullName(Frist_name = "Unknow", last_name ="Forger"):
    print("My name is " + Frist_name + " " + last_name)
myFullName("Anya")
myFullName("Anya", "Forger")
myFullName("Yor", "Forger")
myFullName(last_name = "Forger", Frist_name = "Loid")

def myFruis(Fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["apple", "banana", "coconut"]
myFruis(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))
