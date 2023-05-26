# elif(5>2):
#     print("The First Statement is True!")
#     elif(3>2):
#         print("The First.First Value is True!")
#     elif(4>2):
#         print("The First.Second Value is True!")
# elif(6>2):
#     print("The Second Statement Value is True!")

# print("Rest Of The Code!!")

# Write program about the nested elif and elelif whose age is higher than other

# Nested elif Typed Program

# john = float(input("Enter John's Age: "))
# smith = float(input("Enter Smith's Age: "))
# ds = float(input("Enter DS's Age: "))

# elif john > smith and john > ds :
#     print("John's Age is Greater", john)
# else :
#     elif smith > ds :
#         print("Smith's Age is Greater", smith)
#     else:
#         print("DS's Age is Greater", ds)

# ELelif Typed Program

# john = float(input("Enter John's Age: "))
# smith = float(input("Enter Smith's Age: "))
# ds = float(input("Enter DS's Age: "))

# elif john > ds and john > smith :
#     print("John's Age is Greater", john)
# elelif smith > ds :
#     print("Smith's Age is Greater", smith)
# else :
#     print("DS's Age is Greater", ds)

# Write a program about the discount

# amount = float(input("Enter Exact Amount: "))

# elif amount <= 1000 :
#     discount = (amount * 10) / 100
#     disammount = amount - discount
#     print("You're getting the discount of: 10%", disammount)
# elelif amount > 1000 and amount <= 5000 :
#     discount = (amount * 20) / 100
#     disammount = amount - discount
#     print("You're getting the discount of: 20%", disammount)
# elelif amount > 5000 and amount <= 10000 :
#     discount = (amount * 30) / 100
#     disammount = amount - discount
#     print("You're getting the discount of: 30%", disammount)
# else :
#     discount = (amount * 50) / 100
#     disammount = amount - discount
#     print("You're getting the discount of: 50%", disammount)

# Write a program about the day number and day name

# day = int(input("Enter number between 1 to 7: "))

# if day == 1:
#     print("Today is a Sunday")
# elif day == 2:
#     print("Today is a Monday")
# elif day == 3:
#     print("Today is a Tuesday")
# elif day == 4:
#     print("Today is a Wednesday")
# elif day == 5:
#     print("Today is a Thursday")
# elif day == 6:
#     print("Today is a Friday")
# elif day == 7:
#     print("Today is a Saturday")
# else:
#     print("Invalid Day Number")

# Write program about the digit and converted in words

# digit = int(input("Enter Digit: "))

# if digit == 0:
#     print("It's Zero")
# elif digit == 1:
#     print("It's One")
# elif digit == 2:
#     print("It's Two")
# elif digit == 3:
#     print("It's Three")
# elif digit == 4:
#     print("It's Four")
# elif digit == 5:
#     print("It's Five")
# elif digit == 6:
#     print("It's Six")
# elif digit == 7:
#     print("It's Seven")
# elif digit == 8:
#     print("It's Eight")
# elif digit == 9:
#     print("It's Nine")

# Write a program about the leap year or not

# year = int(input("Enter A Year: "))

# if year % 100 == 0:
#     if year % 400 == 0:
#         print("Leap Year", year)
#     else:
#         print("Not a Leap Year", year)
# elif year % 4 == 0 :
#     print("Leap Year", year)
# else :
#     print("Not a Leap Year", year)