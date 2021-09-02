# list[]: is a combination of values, allows duplicates, heterogeneous objects, 
# is expandable which allows you increase or decrease the size of it as you wish

l = [11, 11.6, "hello", True, 1+2.3j]

print(l)
print(l[0])
print(l[-1])

print("change the values of an item from the list")
l[0] = 300
print(l)

print("add a new item")
l.append("aaa")
print(l)

print("remove that item")

#l.remove(l[-1]) 

l.remove("aaa")

print(l)


l1 = l*2
print(l1)
