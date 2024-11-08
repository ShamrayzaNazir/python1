print("sherry")
print('sherry')

print("this is 'good' for me")

print('this is "good" for me')

print('''this is 'good' for me''')

print('''this is "good" 'and also good' for me''')

print('''this is:
       "good" for me''')



print("shamrayza" , end=" S_ ") # end="" ye likhty hen 2 lines ko 1 line me lany k liye space se space ay gi
print(" Nzair",  "sherry",  "Shakeela", sep=" _ ")


#escape sequance \n

print("Muhammad Nazir \nSherry") #\n use for next line 

print("Muhammad Nazir \tSherry") #\t use for space

print("Muhammad  \"Nazir\" \'Sherry\'")  # \ \ use for "" and ''

print("\u2764")


#variable 
# variable k name 1: nmbr se start ni kr skty or 2: space ni dy skty 3: print ni likh skty

name = "Sherry"
print(type(name))


name = 5
print(name)
#decleration = intilaization


#assi
print("Someone Said \n\tSherry is a 'good' girl\n\tbut\nshe: \n\toften make mistake.")


name = "sherry"
age = 20
email = "binty.sherry"
print("my name is" , name , "my age is" , age , "my email is" , email,) #first method

print(f"my name is {name} my age is {age} my email is {email}") #2nd method


# python me nmbr ko integer mtlb int khty h

number = 1234   # int
print(type(number))
number = 9.0    # float
print(type(number))
number = 2+5j  # complex
print(type(number))


#type casting : this imp information: 1 type ko 2sri me convert krna

number = 3
string = str(number)
print(type(string))  # hr nmbr ko string me convert kr skty hen float ko b but string ko kisi me ni kr skty.

#ex 
number = True
string = str(number)
print(type(string))

#operaters 
#python me ++ or -- ni hota
a = 5
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # // lgany se . k bad wali value ignore krta
print(a**b)
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

a += 12
print(a)
a -= 12
print(a)
a *= 12
print(a)
a /= 12
print(a)

name = (input("write your name :"))
print("the username is ", name)
print(type(name))

#input hmesha str ay gi. us ko int me krny k liye int likhy gy shuru Me.

age = int(input("write your age :"))
print("the age is ", age)
print(type(age))

