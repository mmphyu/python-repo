# Type casting aka type conversion: transforms the value of a data type to another data type

# int(): removes everything after the decimal point, do not round
# can't convert string, complex, etc.
print(int(23.64))
print(int(False))
print(int(True))

# float()
print(float(30))
print(float(True))
print(float(False))

# complex()
# complex(p,q) where p is real part and q is imaginary part
print(complex(8))
print(complex(True))
print(complex(False))
print(complex(39.34))
print(complex(12, -5))
print(complex(12, 5))

# bool(): if 0 and False, False. Otherwise, True.
print(bool(0))
print(bool(1))
print(bool(13))
print(bool(13.23))  
print(bool(23-2j))
print(bool(0+0j))
print(bool("True"))
print(bool("False"))
print(bool("abc"))
print(bool(False))

# str()
print(str(10))
print(str(10+2j))
print(str(True))
print(str(10.5))