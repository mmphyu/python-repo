# represents a group of byte numbers like an array
# only permitted values from 0 to 256 
# is immutable

x1 = [1,5,3,4]
#x1 = [1,2,3,565]

x2 = bytes(x1)

print("Type of x1: ", type(x1))

print("Type of x2: ", type(x2))

for i in x2:
    print(i)

print("x2[-1]: ", x2[-1])
