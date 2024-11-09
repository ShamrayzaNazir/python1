



#  single inheritance syntax

class Father:
    def guide(self):
        print("this is guide method of father class")
    def wprk(self):
        print("the father is worker")



class Children(Father):
    def play(self):
        print(" method of children ")
    def sleep(self):
        print("children sleep")


c1 = Children() # this is call function.
print("\t\t\tthese are children method.")
c1.guide()
c1.wprk()
c1.sleep()
c1.sleep()

# Multiple inheritance

class Father:
    def guide(self):
        print("this is guide method of father class")
    def wprk(self):
        print("the father is worker")


class Mother:   # Father likh k connection bnaya h.
    def protect(self):
        print("Mother protect")
    def cock(self):
        print("Mother cock")

class Children(Father , Mother): # idr dono father Mother kaa connection bnaya.
    def play(self):
        print(" method of children ")
    def sleep(self):
        print("children sleep")


c1 = Children() # this is call function.
print("\t\t\tthese are children method.")
c1.guide()
c1.wprk()
c1.protect()
c1.cock()
c1.sleep()
c1.sleep()

#m1 = Mother()   inko chlany k liye Mother Me father ka connection bnana pry ga. Mother(father)
#m1.protect()
#m1.cock()


# hierarchical inheritance

class Children(Father , Mother): # idr dono father Mother kaa connection bnaya.
    def play(self):
        print(" method of children ")
    def sleep(self):
        print("children sleep")


class Children2(Father , Mother): # idr dono father Mother kaa connection bnaya.
    def play2(self):
        print(" method of children ")
    def sleep2(self):
        print("children sleep")

c1 = Children()
c1.play

c2 = Children2()
c2.guide


# encapsulation
# data ko private krny k liye. 3 types hen.
# 1 private variables  __
# 2 protected Method  _
# 3 private Members  __


class Person:
    def __init__(self , name, age):
        self.name = name
        self.age = age

    def _eat(self):    # ye access ni hoga ku k ye private hoty.
        print("eating")

person = Person("sherry" , 22)

print(person.name)
print(person.age)
print(person._eat)




