s=input("Enter ur Gamil = ")
v=s.find("@")
x=s[:v]
print(x.upper())
b=s[v:]
print(b)
w=len(x) - 2
print(x[0]+"*"*w+x[-1]+b)

