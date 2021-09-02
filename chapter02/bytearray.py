# similar to byte data type beside it is mutable.

x1 = [2,4,7,3]
x2 = bytearray(x1)

for i in x2:
    print(i)

x2[1] = 30

print("Bytearrary has been updated")

for i in x2:
    print(i)