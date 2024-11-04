

# python functions
# jis ko hm ne br br use krna ho usy hm function me rkh dety h.

def even_odd(user_input):
 
 if user_input % 2 == 0:
    print("its even")
 else:
   print("it is odd")

user_input = int(input("write any num"))
even_odd(user_input)



# buitl in function    : ye phly python ne bna k rkhy hoy h.

def print(x): #1
  pass

print("sherry") #2

li = [1,2,3,4]
print(sum(li))



# user_defined function     : apni need se function bnana.

def even_odd(user_input):
 
 if user_input % 2 == 0:
     print("its even")
 else:
   print("it is odd")

user_input = int(input("write any num"))
even_odd(user_input)



#creating a function in python

def fun():
  print("welcome to gfg")


fun()


def add(a,y):
   print(a + y)

add(4,5)

def add(a,y):
   z = a + y
   return z  # Maximum coding Me return use hota.

print(add(4,5))

# parameters
#arguments :    
#def even_odd(user_input):      user_input is called a arguments.


# 1: default arrgument.

def add(a,y):
   z = a + y
   return z  

print(add(4,9)) # error dy ga ku k hmne a ki value di h lkn y ki ni.


def add(a,y ):
   z = a + y
   return z  

num1 = int(input("num 1 :"))
num2 = int(input("num 2 :"))

print(add(num1,num2))


def add(a,y = 2 ):
   z = a + y
   return z  

num1 = int(input("num 1 :"))
num2 = int(input("num 2 :"))

print(add(num1))



# 2: positinol arrhuments.

def intro(name,age, city,grade):
   print(f"my name is{name} and my age is {age} and my city is {city} my grade {grade}")

intro(22 , "sherry"  , "lahore" , "A")  

# 3: keyword arrguments

def intro(name,age, city,grade):
   print(f"my name is{name} and my age is {age} and my city is {city} my grade {grade}")

intro(city = "lahore" , name="sherry" , age = 22 , grade = "A")



# 4: Arbitrary arrguments

def add(*args):   # args means Arbitrary arrguments
   return sum(args) 


print(add(1,2,3,4,5))

# 5: Arbitrary keyword arrguments


def add(**s):
   for x , y in s.items():
      print(f"{x} = {y}")
  # print(s)


# lambda

add = lambda x , y : x + y
print(add(1,2))  

add = lambda x : x**2
print(add(2))  




# docstring

def even_odd(user_input):
  """"this is a function"""    # ye likhny k liye isy docstring khty h.

if user_input % 2 == 0:
    print("its even")
else:
   print("it is odd")

user_input = int(input("write any num"))
even_odd(user_input)
print(even_odd.__doc__)


def add1(x):
   return x**2

add = lambda x : x*2

print(add1)
print(add)


# Assignment


