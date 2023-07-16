#ASCII Codes
# s = "A"
# print(ord(s))
# s1 = " "
# print(ord(s1))
# print(chr(65))

#UNICODES 
# print('\u03b1')
# print('\u03b2')
# print('\u03b3')
# print('\u0385')
# print('\u0904')
# print('\u0915\u0916\u0917')

# Escape Sequence Character \n\r\f\t\v\a\o\x\u
# print("ABC\aDEFGHIJK", end='')

# print('john\'s')
# print("john's")
# print("john\"s")
# print("ABC\\nDEF")
# print(r"ABC\nDEF")
# print('\N{pound sign}')
# print('\N{dollar sign}')
# print('\N{rupee sign}')
# print('\N{superscript five}')

#Print Function Working
# a = 10
# b = "Dhruvin"
# c = 88.89
# print(a, end=" ")
# print(a,b,c)
# print("Hello","World")
# print('Hello'+'World')
# print(a,b,c,sep='-')

# C Style Printing!
# name = "Dhruvin"
# roll_no = 18
# avg = 88.66543

# print("The Student name is %s, his roll no is %d, and his avarage is %f" %(name, roll_no, avg))

# print("Student name is %10s" %(name))
# print("Student name is %-10s and" %(name))
# print("Student avarage is %2.3f" %(avg))

# Place holder style Printing

# a = 22
# b = 7
# c = a/b

# print("The Divison of {0} and {1} is {2}" .format(a,b,c))

# print("The Divison of {2} and {1} is {0}" .format(c,b,a))

# print("The Divison of {0:10} and {1:15} is {2}" .format(a,b,c))

# print("The Divison of {0:<10} and {1:^15} is {2}" .format(a,b,c))

# print("The PI Value is {0:5,}" .format(c))

#Updated Formating
# print(f'The divison of {a:10} and {b:^15} is {c:2.5f}')