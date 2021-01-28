x1="put an ascii file"
x2=x1[::-1]
v=""
for i in range(len(x2)-1):
    y=chr(128-ord(x2[i]))
    v=v+y
print(v)
