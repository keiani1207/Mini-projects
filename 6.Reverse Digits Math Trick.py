num=(input("Enter digit 3 intger = "))
print(num[::-1])

#or
#without converting into strings
num=int(input("Enter 3 digit intger = "))
num0=num//100
num1=num%100
num2=num1//10
num3=num1%10
print(f"{num3}{num2}{num0}")