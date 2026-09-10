Num = int(input("Enter a Number = "))
if Num.isdecimal:
    if Num == 0:
      print("binary representation = 0")
    else:
       while Num > 0:
          remainder = Num % 2
else:
    print("Invalid input!!\nEnter the decimal number only..")