



# Error and exceptions in python.

x = 5
y = "sherry"

try :
    print(x+y)
except :
    print("an error occurred")


print("sherry")

# o division error

x = 5
y = 0
z = "sherry"
try :
   # print(x+z)
    print(x/y)
except ZeroDivisionError as d:
    print(d)
except TypeError as e:
    print(e)
else:
    print("no exception")
finally:
    print("this is Always run.")


# syntax error

try :
    exec("x===5")
except SyntaxError as e:
    print("caught error", e)



x = 5
y = 0
z = "sherry"
try :
   # print(x+z)
    print(x/y)
    print(x+y)

except Exception as e:  # exception jenrel error btata. hr type k error ko caught kr leta.
    print(e)
else:
    print("no exception")
finally:
    print("this is Always run.")


 # erase error

use = int(input("enter your age"))
#if type(user) == str:
  #  raise ("this is not ")


# file handling

#r = open("file ka name den gy read krny k liye" , "r")
#content = r.read()
#r.closed()
#print(content)

# w = open("file open k liye file ka name likhy gy" , "w")
#w.write("this is new data")
#w.closed()
#print(content)


w = open("file1.txt " , "w")
w.write("new file created")
w.close    # file bn gai is se file1.txt 

a = open("file1.txt", "a")
a.write("\nthis is 2nd data")
a.close


r = open("file1.txt" , "r+")
r.write("this written using r+")
r.seek(0)
content = r.read()
print(content)
r.close()


# withopen   file ko read krny k liye. is se close ni krni prti.

with open("file1.txt" , "r")as r:
    content = r.read()
    print(content)


with open("file1.txt" , "r")as r:
    r.write("\nsherry")
    r.seek(0)
    content = r.read()
    print(content)



    