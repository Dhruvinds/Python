# write a program 10 times hello
# Write a program for number of times

# count = 0

# while count < 10:
#     print(count + 1, "Hello")
#     count += 1

# Write a program to reverse the number
# Program Runs Until the conditions are met

# number = int(input("Enter a Number: "))

# while number > 0:
#     r = number % 10
#     number = number//10
#     print(r)


# Write a program to display multiplication table

# num = int(input("Enter a digit: "))
# i = 1

# while i <= 10:
#     mul = num * i
#     print(num, "*", i, "=", mul)
#     i = i + 1

# Write a program about the counting the number of digit in a number

# number = int(input("Enter a Number: "))
# counter = 0

# while number>0 :
#     number = number//10
#     counter = counter + 1

# print("The Numbers of a digits are: ", counter)

# Write a program about the find the sum of digit in a number

# number = int(input("Enter a Number: "))
# sum = 0

# while number > 0:
#     r = number%10
#     number //= 10
#     sum = r + sum

# print("The Sum of Number is: ", sum)

# Write a program about the reversing the number

# num = int(input("Write a Number: "))
# rev = 0

# while num > 0:
#     r = num % 10
#     num = num // 10
#     rev = rev * 10 + r

# print("The Reverse Number is: ", rev)

# Write a program and check it is a palidrome or not

# num = int(input("Write a Number: "))
# org_number = num

# rev = 0

# while num > 0:
#     r = num % 10
#     num = num // 10
#     rev = rev * 10 + r

# if org_number == rev :
#     print("It is a Palidrome")
# else :
#     print("No it is not a palidrome")

# print("The Reverse Number is: ", rev)

# Write a program find sum of given number as a input

# no_of_no = int(input("Enter no: "))
# sum = 0
# count = 0

# while no_of_no > count:
#     n = int(input("Enter a number: "))
#     sum = sum + n
#     count += 1
# print("The sum of number is: ", sum)

# Write a program about the sum of positive and negative number

# no_of_no = int(input("Enter no: "))
# psum = 0
# nsum = 0
# count = 0

# while no_of_no > count:
#     n = int(input("Enter a number: "))
#     if n < 0:
#         nsum = nsum + n
#     else:
#         psum = psum + n
#     count += 1
# print("The sum of Positive number is: ", psum)
# print("The sum of Negative number is: ", nsum)

# Write a program Find the maximum number from the given number

# no_of_no = int(input("Enter a no of no: "))
# # max = 0 --> Positive number only
# max = int(input("Enter max number: "))
# count = 0

# while no_of_no - 1 > count:
#     n = int(input("Enter a no: "))
#     if n > max:
#         max = n
#     count += 1
# print("The Max is", max)

# Write a program to convert decimal number to binary

# num = int(input("Enter a number: "))
# bin = ''

# while num > 0 :
#     r = num % 2
#     num = num // 2
#     bin = str(r) + bin

# print(bin)

# Write a program about the guess the number between 0-10

# import random

# num = random.randint(0,9)
# guess = 0

# while num != guess :
#     guess = int(input("Enter Your Guess Number: "))
#     if guess < num :
#         print("The Number is Smaller")
#     elif guess > num :
#         print("The Number is Bigger")
#     else :
#         print("Correct, You Got the Right Number!")

# Infinite Loops Break -- Countinue --- Pass

# while True:
#     print('Hello')

# USE OF BREAK STATEMENT

# while True:
#     num = int(input("Enter a Number: "))
#     if num > 0:
#         print("Positive")
#     elif num < 0:
#         print("Negative")
#     else:
#         break;

# count = 0

# while count < 10:
#     print(count)
#     count += 1
#     if count > 5:
#         break

# USE OF COUNTINUE STATEMENT

# count = 0

# while count < 10:
#     num = int(input("Enter a Number: "))
#     if num % 3 == 0 :
#         # continue --> That mean simple program start with first line of the loops
#     print(num)
#     count += 1

# USE OF PASS STATEMENT

# count = 0

# while count < 10 :
#     num = int(input("Enter a Number: "))
#     if num % 3 == 0:
#         pass --> Do Nothig
#     else :
#         print(num)
#     count += 1

# Method Two Without Pass

# count = 0

# while count < 10 :
#     num = int(input("Enter a Number: "))
#     if num % 3 != 0 :
#         print(num)
#     count += 1

# ELSE SUITE

# count = 1

# while count <= 10 :
#     print(count)
#     count += 1
# else :
#     print("Printed all 10 Numbers")

# print("End of the program!")

# Abruptly Stoped the program using break

# count = 1

# while count <= 10 :
#     print(count)
#     count += 1
#     if count > 5 :
#         break
# else :
#     print("Printed all 10 Numbers")

# print("End of the program!")

# FOR LOOP

# msg = "DHRUVIN"

# for x in msg :
#     print(x)

# For Loop with Range function

# for i in range(0, 10):
#     print(i)

# for i in range(5, 10):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# Write a program Display Multiplication table for a number

# num = int(input("Enter a Number: "))

# for count in range(1, 11):
#     print(num, "*", count, "=", num * count)


# Write a program Find the factorial of a given number

# num = int(input("Enter a Number: "))
# fact = 1

# for count in range(1,num+1):
#     fact = fact * count
# print("The Factorial of the", num, "is:", fact)

# Print N Terms of AP --> Arithmetic Progression Series

# a = int(input("Enter value of A: "))
# d = int(input("Enter value of D: "))
# n = int(input("Enter value of N: "))

# for t in range(a, a + n * d, d):
#     print(t)

# Print N Terms of Fibonacci Series

# n = int(input("Enter a number: "))
# a = 0
# b = 1

# for t in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# Find the factor of number

# n = int(input("Enter a Number: "))

# for i in range(1, n+1) :
#     if n % i == 0 :
#         print(i)

# Check if number is prime or not

# n = int(input("Enter a Number: "))
# count = 0

# for i in range(1, n+1) :
#     if n % i == 0 :
#         count += 1
# if count == 2 :
#     print("The Number is Prime")
# else :
#     print("The Number is Not Prime")

# FOR LOOP BREAK STATEMENT

# for i in range(0,10) :
#     if i > 5 :
#         break
#     else :
#         print(i)

# FOR LOOP ELSE STATEMENT

# for i in range(0,10):
#     print(i)

# else :
#     print("The Statement Else has executed")

# FOR LOOP PASS STATEMENT

# for i in range(0,10):
#     pass
# print("Rest Of the code will excecuted")

# FOR LOOP BREAK STATEMENT
# for i in range(0,10):
#     if i % 5 == 0 :
#         continue
#     print(i)

# NESTED LOOP USING FOR LOOPS

# for i in range(0, 5):
#     for j in range(0, 5):
#         print('(', i, j, ')', end=" ")

# s1 = "ABC"
# s2 = "XYZ"

# for i in s1 :
#     for j in s2 :
#         print(i,j,end=" ")
#     print("")

# Print Prime number from 1 to 100

# for n in range(1, 100+1):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print(n)

# Patterns

# for i in range(0, 5):
#     for j in range(0, 5):
#         print('*', end=" ")
#     print('')

# for i in range(0, 5):
#     for j in range(0, 5):
#         if i >= j:
#             print('*', end=" ")
#     print('')

# for i in range(0,5):
#     print('* ' * 5)

# for i in range(5,0,-1) :
#     print("* " * i)

# Match Case

day = int(input("Enter a number: "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Holiday")
