# Variable and gives direct value to the string that means it works like literals

# s1 = 'Hello'
# s2 = "Hello"
# # s3 = 'John's'
# s3 = "John's"
# s4 = '''Hello
#         How Are You'''

# for x in s4 :
#     print(x)

# print(s2[1])
# print(s2[-1])
# print(s4)

# Operators on String
#1. Concatenation 2. Repetition 3. Indexing 4.Slicing 5. in 6. Not in

# 1. Concatenation
# s1 = "Hello"
# s2 = "World"

# s3 = s1 + " " + s2
# print(s3)

# s1 = "How " + "Are " + "You"
# print(s1)

# s1 = "Hello" + str(15)
# print(s1)

# 2. Repetition

# s1 = "Dhruvin"
# s2 = s1 * 4
# print(s2)

# 3. Indexing
# Sequence or array of character
# s1 = "Hello World"
# for x in s1 :
#     print(x)

# Range based indexing
# s2 = "How Are You!"
# for i in range(0, len(s2)) :
#     print(s2[i])

# Reverse String Printing

# s1 = "Hello World"
# print(len(s1))

# for i in range(len(s1)-1, -1, -1) :
#     print(s1[i])

# Printing of skipping 1 number

# for i in range(0, len(s1), 2) :
#     print(s1[i])

# 4. Slicing
#string[start:end:step] optional

# s1 = "Hello World"

# print(s1[0:12:1])
# print(s1[::1])
# print(s1[0:len(s1):1])
# print(s1[-1:-len(s1)-1:-1])

#5 IN
# s1 = "Dhruvin Sorathiya"
# s2 = "D" in s1
# print(s2)

#6 NOT IN
# s3 = "H" not in s1
# print(s3)

# Relational Operators in Strings
#Comparing String
#1 The string matched which letter will come in dictionary the letter come first it is smaller and the come after it is bigger!

#2. The capital letter is smaller and the smaller letter is bigger

# s1 = "Alaska"
# s2 = "Canada"
# s3 = s1 < s2
# print(s3)

# s1 = "Canada"
# s2 = "canada"
# s3 = s1 > s2
# print(s3)

# print(dir(str)) --> Methods of String
# Introduction To String Method

# Class - Definition/Design  and Object (It's Instance) String is an object

# Design of a car -> car is an Object and design is a class

# Class contain data and operation/functions --> len(s) -> Contain data and do operation on functions so it means we call it methods

# s1 = "Hello, How are you!!"
# print(type(s1))

# print(help(s1.endswith)) -> Check of the methods

# Find and Index Methods
# s1 = "Hello, How Are You"
# print(s1.find('o'))
# print(s1.find('How'))
# print(s1.find('K'))
# print(s1.find('o',5))
# print(s1.find('o',5,8))
# print(s1.find('o',9,17))

#rfind method
# print(s1.rfind('o'))
# print(s1.rfind('o',0,7))
# print(s1.rfind('Canada'))

#Index Method
# print(s1.index('o'))-> it finds only indexing, and if not there any letter the index gives an error

#rindex
# print(s1.rindex('Are'))

#Count 
# print(s1.count('o'))
# print(s1.count('l'))

# s1 = "Python"
# Removing Spaces
# print(s1.ljust(10))
# print(s1.rjust(10))
# print(s1.center(10))
# print(s1.center(20,'@'))

# s1 = "    Python   "
# print(s1.strip())
# print(s1.lstrip())
# print(s1.rstrip())

# Methods of cases
# s1 = "hello Dear!"
# s2 = 'hello Dear How are you!'
# print(s1.capitalize())
# print(s2.lower())
# print(s2.upper())
# print(s2.swapcase())
# print(s2.title())
# print(s2.casefold())

# s1 = 'heLLo'
# s2 = 'HELLO'
# print(s1.lower() == s2.lower())

# s1 = 'Bu\u00DF' --> "Buss"
# print(s1)

# s2 = "Buss"
# print(s1 == s2)
# print(s1.lower() == s2.lower())
# print(s1.casefold() == s2.casefold())

