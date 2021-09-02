# frozenset(): similar to set data type but it is immutable and not expandable.

x1 = {2,"hello",3.2}
x2 = frozenset(x1)

print(type(x2))

for i in x2:
    print(i)