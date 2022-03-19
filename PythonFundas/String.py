# string

mes = 'hello world' # variable names sholud be readable

singlequotes = "boby's world" # single quotes

multiline = """ this is a multi 
line
confirm!!!
"""
print(mes) # hello world
print(mes[0]) # h
print(mes[:6]) # hello ( starting to (len-1))
print(mes.lower())
print(mes.upper())
print(mes.count('l'))
print(mes.find('world'))
print(mes.find('notfound'))

# ouput -->
"""
hello world
HELLO WORLD
3
6
-1
"""

new_message = mes.replace('world','universe')

print(new_message)

name = 'arjun'
greeting = 'hello'

print(f'{greeting} {name.upper()}')

# ouput -->

"""
hello universe
hello ARJUN
"""

print(dir(mes))

print(help(str))
