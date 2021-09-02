# set{}: the combination of values as a single entity.
# It does not permit duplicate values, is mutable, permits heterogeneous objects.
# It is also expandable: add or remove items.
# It can not be accessed by index.

x = {1, "hello", 23.4, 2-1j}
print(x)

print("Add a new item")
x.add(2)
print(x)

print("remove an item")
x.remove(2)
print(x)

for i in x:
    print(i)
