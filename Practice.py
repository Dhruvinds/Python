# 1. Write a Program to print "Hello, World!"
# print("Hello, World!")

# 2. Write a Program to Print Integer Number Entered by User
# int_number = int(input("Enter Integer Number: "))
# print("The Integer Number is:", int_number)

# 3. Write a Program to Add Two Integer Numbers Entered by User
# a = int(input("Please Enter The value Of A:"))
# b = int(input("Please Enter The value Of B:"))

# print("The sum of two number is:", a+b)

# 4. Write a program where the user is asked to enter two integers (divisor and dividend) and the quotient and the remainder of their division is computed.(Both divisor and dividend should be integers.)

# divisor = int(input("Enter Value of Divisor:"))
# dividend = int(input("Enter Value of Dividend:"))

# quotient = int(divisor/dividend)
# remainder = int(divisor % dividend)

# print(quotient)
# print(remainder)

# 5. Find Size of int, float, double and char in your Computer

# import sys

# print("The Size of the int, Float, Double and Char is:", sys.getsizeof(int),sys.getsizeof(float),sys.getsizeof(chr),sys.getsizeof(bool) )

# a = int(input(""))
# print("The size of integer is:", sys.getsizeof(a))

# 6.Write a Program to Swap Two Numbers

# x = int(input("Please Enter the value of X:"))
# y = int(input("Please Enter the value of Y:"))

# x, y = y, x

# print("Swapping Value of X:", x)
# print("Swapping Value of Y:", y)

# 7.Write a Program to Find ASCII Value of a Character

# value = input("Please Enter Any Character:")

# print("The ASCII Value of that character is:" , value ,ord(value))

# 8. Write a Program to Multiply two decimal Numbers entered by User

# a = float(input("Please Enter Decimal Number of A:"))
# b = float(input("Please Enter Decimal Number of B:"))

# print("The Multiply Value of A and B is:", a * b)

# IF ELSE QUESTION SOLUTION

# 1.  Write a Program to Check Whether Number is Even or Odd

# a = int(input("Enter any number: "))

# if (a % 2) == 0 :
#     print("You have entered a even number")
# else:
#     print("You have entered a odd number")

# 2. Write a Program to Check Whether a Character is Vowel or Consonant

# char = input("Please Enter the character: ")

# if (char == 'a'or char == 'e' or char == 'i' or char == 'o'or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
#     print("You Have Entered the Vowel")
# else:
#     print("You Have Entered the Consonant")

# 3. Write a Program to Find Largest Number Among Three Numbers entered by users

# n1 = int(input("Entered The First Number: "))
# n2 = int(input("Entered The Second Number: "))
# n3 = int(input("Entered The Third Number: "))

# if ((n1>n2) and (n1>n3)):
#     print("The Number 1 is bigger")
# elif ((n2>n1) and (n2>n3)):
#     print("The Number 2 is Bigger")
# else:
#     print("The Number 3 is bigger")

# 4. Write a Program which accepts coefficients of a quadratic equation from the  user and displays the roots (both real and complex roots depending upon the discriminant).

# import cmath

# a = float(input("Enter Value"))
# b = float(input("Enter Value"))
# c = float(input("Enter Value"))

# discriminant = b * b - 4 * a * c

# if (discriminant> 0) :
#     x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
#     x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
#     print("Roots are real and different")
#     print("The X1 is the: ", x1)
#     print("The X2 is the: ", x2)
# elif (discriminant == 0) :
#     print("Roots are real and same")
#     x1 = -b/(2*a)
#     print("X1 = X2 =", x1)
# else :
#     realPart = -b/(2*a)
#     imaginaryPart =cmath.sqrt(-discriminant)/(2*a)
#     print("Roots are complex and different") 
#     print("x1 = ", realPart , "+" , imaginaryPart,"i" )
#     print("x2 = ", realPart, "-" , imaginaryPart,"i")

# 5.  Write a Program to Check whether a year entered by user is Leap Year or not

# leap year == 366 days
# No Leap Year == 365 days

# year = int(input("Enter the Year: "))

# if ((year % 400 == 0) and (year % 100 == 0)) :
#     print(year, "Is a Leap Year")
# elif ((year % 4 == 0) and (year % 100 != 0)) :
#     print(year, "Is a Leap Year")
# else:
#     print(year, "Is Not a Leap Year")



