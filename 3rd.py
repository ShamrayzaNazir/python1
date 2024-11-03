



# loops   loops i table py chlty hen.....
# for in loop

name = "sherry"  

for character in name:
    print(character)

number = [1,2,3,4,5,6,7,8]
for character in number:
    print(character)  #simple loop

    # for range loop

for x in range(1,10):
    print("Atif")

for x in range(1,10,2):
    print(x)

#for x in range(1,101):
  #  print(x)

s = "geeks"
for i in s:
    print(i)

for i in range(0,10,2):
 print(i)

# enumerate

name = "iqra "
for char in name:
    print(char)

for index , char in enumerate(name):
    print(index,":", char)

# nested for loop


for x in range(1,4):
    for y in range(1,4):
        print(x,y)


# while loop


count = 0
while (count < 3):
    print("hello sherry")
    count = count + 1  # count += 1    ye count ko false krna zroori h.



# control statements


for x in range(1,10):
    if x == 5:     # 5 skip ho jay ga
        continue
    print(x)

for x in range(1,10):
    if x == 3:     # 3 skip ho jay ga
        continue
    print(x)

#break statement

for x in range(1,10):
    if x == 3:    
        break
    print(x)



#Assignment
for x in range(7,77,7):
    print (x)

# table assignment

user_input=int(input())
for x in range (1,11):
     print(f"{user_input} x {x} = {user_input*x}")


# * print
for x in range(1,4):
    print("*****")


#for x in range(1,101):
    
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)



year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
         if year % 600 == 0:
            print("leap year")
        else:
            print("not leap year")    





    



