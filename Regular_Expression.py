#Regular expression is usefull for defining patterns and string matching.

from re import *

# print(match('a', 'a').group())
# print(match('a|b', 'a').group())
# print(match('a|b', 'b').group())
# print(match('abc', 'abc').group())
# print(match('abc', 'abcd').group())
# print(match('[abc]', 'abcd').group())
# print(match('[abc]', 'bcd').group())
# print(match('[abc]+', 'bcd').group())
# print(match('[abc]+', 'bbbbbbbb').group())
# print(match('[abc]+', 'ababcababaca').group())
# print(match('[abc]{5}', 'ababcababaca').group())

# Special Character for Reg Ex

# print(match('[a-z]+', 'python').group())
# print(match('[a-z]+', 'dhruvin').group())
# print(match('[^a-z]+','AB@#$%^').group())
# print(match('([a-z]+)|([A-Z]+)' , 'ABCd').group())
# print(match('([a-z]+)|([A-Z]+)', "abcD").group())

# print(match('^Hell', 'Hello').group())

# x = r'rld$'
# c = compile(x)
# r = c.search("Hello World")
# print(r.group())