


# OOP. real life ko object ko apni coding me copy krny k liye opp use hota h.
# oop me 2 chezen hoti hen. class and object.
# class
# class ko use krty hoy object bnaty hen.
# Attributes. 
# Actions.

class Dog:                  # this is class.
    breed = "german"
    colur = "black"
    age = 3

    def bar(self):          # this is Actions.
        print("the dog barks")
    def run(self):
        print("the dog runs")
    def sleep(self):
        print("the dog sleep")


d1 = Dog()
print(d1.breed)
print(d1.colur)
print(d1.age)

d1.bar()
d1.run()
d1.sleep()



class Human:
    name = "sherry"
    age = 22
    gender = "female"

    def eat(self):
        print("she is eating")
    def sleep(self):
        print("she was sleeping")
    def write(self):
        print("she is writting")


h1 = Human()
print(h1.name)
print(h1.age)
print(h1.gender)

h1.eat()
h1.sleep()
h1.write()

# 2nd  with  consector. the consector is __int__

class dog:
    def __init__(self , breed , colour , age): # self likhny k bger inko Access ni kr skrty.
        self.breed = breed
        self.colour = colour
        self.age = age
    

    def bark(self):
        print("woof")
    def run(self):
        print("running")
    def eat(self , meal):
        print("eating" , meal)
    
d1 = dog("german" , "black" , 10 )
d2 = dog("russain" , "gray" , 12)
d3 = dog("russain" , "white" , 18)

print(d1.colour)
print(d1.breed)
print(d1.age)

d1.bark()
d1.run()
d1.eat("meal")


print(d2.age)
print(d2.breed)
print(d2.age)

d2.bark()
d2.run()
d2.eat("meal")



print(d3.age)
print(d3.breed)
print(d3.age)

d3.bark()
d3.run()
d3.eat("meal")


