#Currency Splitter
dollar =int(input("Enter amount in dollar = "))
x=dollar//100
y=dollar%100
z=y//50
a=y%50
b=a//20
c=a%20
d=c//1
print(f"{x} $100 dollar {z} $50 dollar {b} $20 dollar {d} $1 dollar")

