

li = [1,2,3,4,["a","b","c", [12,13,14]]]  # this is called two dimentional. 2d

for x , y in enumerate(li):
    print(x,y)

print(li[4][3][2])


# Dictionries in python

dic = {"a" : 1, "b":2 , "c" :3}   # value koi b dy skty h.
dic2 = {"a" : [1,2,3], "b":(1,2,3) , "c" : {"d":[5,6,7]}}

print(dic2["c"]["d"][2])

print(dic)

print(dic["b"])

# empty dic

dic3 = {}
dic3["a"] = int(input("write any nmb"))
dic3["2"] = 2
dic3["c"] = 3
dic3["d"] = 4

print(dic3)

# list se dic bnana.

dic = dict([(1,"a"),(2,"b"),(3,"c")])
print(dic)
# del dic[1]
#print(dic)
print(dic.clear())


# 1 jesi value deny k liye.

tu = ("a" , "b", "c")
print(dict.fromkeys(tu, "sherry"))

# index na hony ki surt me eror ki bjay none de de ga. .grt is liye use krty h.
dic = dict([(1,"a"),(2,"b"),(3,"c")])
print(dic)
print(dic.get(1))


# .pop kisi nmbr ko remove k liye is me nmbr likhna prta h.   li me auto last wala ho jata remove.
d = {1:"001" , 2:"010", 3:"001"}
print(d.get(4,"not found"))
d.pop(2)
print(d)
d.popitem()   # last wala nmbr remove ho jay ga afr koi value na di ho dic me. 
print(d)

# li me auto last wala ho jata remove
li = [1,2,3,4,5]
li.pop()
print(li)

# update method in dic.

d1 = {1:"001" , 2:"010", 3:"001"}
d2 = {4:"a" , 5:"b", 6:"d" }
print(d1)
d1.update(d2)
print(d1)

# setdefault fun in dic.

d3 = {4:"a" , 5:"b", 6:"d" }
print(d3.setdefault(3 , "g"))
print(d3)


#  keywords arbitrary arguments.

def add(**a):
    print(a)

add(a = 1 , b = 2 , c = 3)

# arbitrary arguments.

def add(*a):
    print(a)

add(1,2,3) # ye tuple return krta h.



d4 = {1:"a" , 2:"b" , 3:"c"}
print(d4.keys())
print(d4.values())
print(d4.items())

# loop on dic.

for x , y in d4.items():
    print(x,y)


# list se dic me convert krny ka treqa.

dic = {}
li = ["a","b","c"]
for x , y in enumerate(li):
    print(x,y)
    dic[x] = y
    
print(dic)