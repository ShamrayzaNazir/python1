



# non premitive data type
# list

li = [1,2,3,4,5,"sherry" , 5.5, True]
lenght = len(li)
print(lenght)


print(li[1])
print(li[1:5])
print(li[1:5:2])
li.pop()
print(li)

print(li[-1])

# list k functions

li = [34,4,5,"iqra", True]
li2 =["a","b","c"]
li2 = [1,2,3,4,5]


# insert

li.insert(1,"atif")
print(li)

#append

li.append(10)
print(li)

# extend

li.extend(li2)
print(li)


# remove

li.remove("iqra")
print(li)

# pop

li.pop(4) # end se remove krta
remove_ele = li.pop(4)
print(remove_ele)
print(li)

# clear

li.clear()
print(li) # all chezen clear kr deta.

# delete

#del  li[1]
#print(li)

# count

li.count("iqra")
print(li)

# copy
li2.copy()
print(li2)

# sort

li2.sort()
print(li2)

# reverse
li2.reverse()
print(li2)

# index

li2.index(2)
print(li2)

# max

max = max(li2)
print(max)

# mini

min = min(li2)
print(li2)

# sum 
sum = sum(li2)
print(sum)

#  tuple
tu = (1,2,3,4,4, "sherry" , 5.6)
count = tu.count(4)
print(count)


li = []
for x in range(3):
    user_input = int(input(f"yourname :"))
   # li.append(user_input)
print(tuple(li))  # list ko tuple me change kiya.



tu1 = (1,2,3,4)
tu2 = (1,2,4,5)
tu3 = (tu1 , tu2)
print(tu1+tu2)
print(tu1 * 2)
print(tu3)



# Assignment




