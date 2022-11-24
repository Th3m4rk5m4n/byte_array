a=bytearray(b'\xDE\xAD\xBE\xEF')
a[0]=0

print(a)
print(type(a))
print(a[0:2])

a.append(5)
print(a)

