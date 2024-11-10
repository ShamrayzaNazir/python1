



# polymorphisam 
# types
# Method overloading 

class Addition(object):
    def add(self ,x,y):
        return x+y
    def add(self ,x,y,z):
        return x+y+z
    def add(self ,a,b,c,d):
        return a + b + c + d   # end wala dono upr walo ko over load kr deta .
    def add(self , *a):
        return sum(a)

a1 = Addition()
print(a1.add(2,4,5,6))


# Method overriding

class Animal:
    def sound(self):
        print("some animal sound")
    def eat(self):
        print("eating")

class Dog(Animal):
    def sound(self):
        print("woof! woof!")

class Cat(Animal):
    def sound(self):
        print("meow!")


c1 = Animal()
c2 = Dog()
c3 = Cat()

c1.sound()
c2.eat()
c2.sound()
c3.sound()



# Abstraction   , kisi chz ko hide krna. jesy car ka injin.

from abc import ABC, abstractmethod 

class Car(ABC):
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

@abstractmethod 
def print(self):
    pass

def accelerate(self):
    print("speed up......")

def stop(self):
    print("stopped.")


class Hatchback(Car):
    def printdetails(self):
        print("brand" , self.brand)
        print("model" , self.model)
        print("year"  , self.year)

    def sunroof(self):
        print("not having this feature.")

car = Hatchback("Maruti" , "Alto" , "2024")
car.printdetails()
car.sunroof()



class Suv(Car):
    def printdetails(self):
        print("brand" , self.brand)
        print("model" , self.model)
        print("year"  , self.year)

    def sunroof(self):
        print("not having this feature.")


s1 = Suv("honda" , 2022 , 2024)


#z1 = Hatchback()
#z1.brand()
#z1.model()
#z1.year()




