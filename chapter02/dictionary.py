# dict{}: denotes a group of values as key-value pairs
# duplicate key does not allow but duplicate value does
# when a new value with existing key is inserted, the existing value will be replaced.
# It allows key to be string data type.

x = {1: "Mon", 2: "Myat", 3:"Phyu"}
print(type(x))
print(x)

x[4] = "student"
print(x)

del x[4]
print(x)