



#input function

#name = input("write your name : ")
#print("your name is : " + name)

#age = input("write your age: ")
#print("your age is :" + age)
#age_int = int(age)
#print (type(age))
#print(type(age_int))       7 to 14 khud # kiya h.


# string : every nmbr or word in "" is called string

# indexing
name = "sherry"
for z,y in enumerate(name):
    print(f"{z} : {y}")
# print(name[2]) # index fined krny k liye : index 0 se start hota h or negtive -1 se.


#slicing
# name [ start : end - 1 : stop]

name1 = "sherry iqra laiba atif sharib"
#print(name[0] , end="")
#print(name[1] , end="")
#print(name[2] , end="")
#print(name[3] , end="")
#print(name[4] , end="")
#print(name[5] , end="") # inki need ni


print(name1[0:6])
print(name1[:8])

#stepping
name2 = "12345678910"
print(name2[0:5:2])
print(name2[::3])
print(name2[::])
print(name2[::-1])
print(name2[::-3])

#assignment

intro = "my name is sherry and my age is 22 and my qualification is Master"

print(intro[11:17] , intro[32:34] , intro[59:65])

numbers = "123456789"
print(numbers[1::2])

#sentex    
# name.upper()
name3 = "sherry bhatti"
print(name3.upper())
print(name3.lower())
print(name3.title())
print(name3.capitalize())
print(name3.swapcase())
print(name3.center(20 , "_"))
print(name3.count("r"))
print(name3.endswith("bhatti"))
print(name3.expandtabs(20))
print(name3.find("a"))  #index b same h find k.
print("-" .join(name3)) 


li = list(name3)
name5 = "".join(li)
print(name5)
print(li)



#immutable data type string
name4 = name3.upper()
print(name3)
print(name4)

#git commit -m "first commit"


name6 = "shamrayza"
li = list(name6)
li.pop()  # pop se last wala word khtm ho jata
name7 = "".join(li)
print(name7)
print(li)

# python stateMent
# types: if , if else, elif, nested, ternary|short hand

#if
i = 10 
if i != 10 :
    print("i is") # false ki output ni mily gi.


#if else
i = 10 
if i == 10 :
    print("i is")  
else:
    print("i is not")


i = 10 
if i != 10 :
    print("i is")   
else:
    print("i is not")


#elif

i = 25
if i == 10:
    print("no")
elif i == 20:
    print("nooo")
elif i ==15:
    print("no way")
elif i==25:
    print("yes it is")
else:
    print("this is not")

i = 10
if i==10:
    print("parent if")
    if i > 5 :
        print("child if")
    else:
        print("child else")
else:
    print("parent else")


    # Assignment

marks = 90
if marks >= 90 :
    print("A")
if marks >= 80:
    print("B")
if marks >= 70 :
    print("B+")
if marks >= 60:
    print("C")
else:
    print("flase")
    











