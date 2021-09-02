# range(): denotes a sequence of number and is immutable.

x = range(3)
for i in x:
    print(i)

print("Range with starting point 2")
y = range(2,6)
for i in x:
    print(i)

print("Range with increment 2")
z = range(0,6,2)
for i in x:
    print(i)

print("Access items by index")
print(z[-1])