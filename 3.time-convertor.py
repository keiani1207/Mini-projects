#Time Converter
TS=int(input("Enter The Total Number Of Seconds = "))
x=TS//3600
a=TS%3600
y=a//60
b=a%60
print(f"{x} Hours {y} Minutes {b}seconds")