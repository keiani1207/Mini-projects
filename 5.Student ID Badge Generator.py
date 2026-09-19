#Student ID Badge Generator
first_name = input("enter your first name = ")
last_name = input("enter your last name = ")
birth_year = int(input("enter your birth year = "))
print(f"---------------------------\nSTUDENT BADGE\nNAME: {first_name} {last_name}\nYEAR OF BIRTH: {birth_year}")
x=first_name[0] +last_name.upper() +"_" + str(birth_year)
print(f"USER ID: {x}\n--------------------")
