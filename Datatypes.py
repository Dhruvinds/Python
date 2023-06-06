# Variables in Python 
# 1. Data -> a program contain data (in every Programming Language)
# 2. Instructions -> a program contain set of instruction (in every Programming Language)

# a = 10  whenever you have declare that variable you have to assign the value with it.
# print(a) you can't took variable without data

# Multiple Value assign to that variable

# name, price, weight = 'Soap', 20, 50
# print(name)

# if i have to assign same value to every variable 

# a = b = c = 1
# print(c)

# Python Dynamically typed Language
# in python we dont have define datatype but in python it will defined by itself only

# a = 10
# print(type(a))

# a = 'Dhruvin'
# print(type(a))

# a = 18.75
# print(type(a))

# Rules of declaring the variables name 
# name can contain alpha numeric characters and underscore 
# roll_number , roll , rollno1, cust_name

# name should start with a letter or underscore character
# _custname , customer

# keyword should not be used as a name of the variables
# import keyword
# print(keyword.kwlist)

# variables are case sensitive
# a = 10 and A = 10 are different

# python data type 
# 1. Numeric -> Int (10), Float(10.20), Bool(true,false), Complex(a+ib)

# 2. Sequence -> list (mutable, modified)[1,2,3,4,5], tuple (unmutable, unmodified, readonly) (1,2,3,4), string ('dhruvin') it's in index type string, bytes(0-255, unmutable, unmodified), bytearray(mutable, modified)

# 3. Set -> set {2,3,5,6} (unorder value, no repeation in value), frozenset(freeze value)

# 4. Dictionary -> dict(key, value ) -> name : 'Dhruvin'

# int and float data types

# x = 1234567898765434556677
# print(x.__sizeof__())

# x = 1245E-2 --> 12.45--> 1245 * 10^2
# print(x)

# Bool and Complex Datatypes

# a = True
# print(type(a))

# a = complex(5+9j)
# a = complex(12,9)
# print(a)
# a = 3 + 5j
# print(type(a))
# print(a.real)
# print(a.imag)

# Literals in Python!
# Literal is just the fixed value of the data types
# a = 123_45_678
# a = 12_3.45
# a = complex(12_3.45 + 67_89.87j)
# print(a)

# Number system -> decimal, 0b101 binary (0-1), 0o10 octal (0-7), 0xA hexadecimal (0-15 (0-F))

# a = 0b101
# b = 0o5
# c = 0x5
# print(a,b,c)

# a = int(input("Enter Number"),2,8,16)
# print(a)

# Base Conversion in Python
# a = 16
# print(bin(a))
# print(oct(a))
# print(hex(a))
# print(bin(16))
# print(oct(20))


