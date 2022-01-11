print('arjun'+'20')

print(3*'arj')

print(ord('A'))

print(chr(65))

print('arjun' >= 'Arjun')

print(True <= 1)

# print(10<'arjun') # error

print(10 < 20 < 30 < 40)
print(10 < 20 < 30 < 40 > 50)  # False

print(10 == 'ar')  # False # content comparison

print(10 is 20)  # reference comparasion

"""
for non boolean type

x and y

if x evaluates true then result is y
if x evaluates falsethen result is x

"""

print(10 and 20)  # 20

print('' and 'arj')  # ''

print(10 or 20)  # 10

print(not 'arj')  # False

print(++10)  # not increment operators 10


print(--10)  # 10


"""
-- no increment and decrement operator

"""

print(20+30j)

print(30 if 20 > 10 else 40)  # ternary operator

# operator precedence

# () ** *      /,%.// - all has same pref  + -


"""
module - consists of classes var and function
if we have 2 mod python takes the recent one (no eroor)

if we have 2 fucn new one given priority


- math module

dir(math)

module alias - as keyword

from math import sqrt
from math import sqrt as s,pi as p

"""

# how to read input and 

x = input('enter the number')

"""


"""

x,y = map(int,input().split(','))
print(x,y)

# list comprehension
# list unpacking

s1 = '10 20'
splitt = s1.split()
newlist = [int(x) for x in splitt]
print(newlist)

num = eval(input('enter the number'))
print(type(num), num)

"""
dynamically gives the int float and dict
alternative to type cast

"""

# command line arguments

from sys import argv

for i in argv:
    print(i)

print(len(argv))

"""
int + str == type error

py test.py "arjun ava" >> command line arguments
"""

# print()  --> \n

print("arj",end="**")
print()
print('hunk','angle',sep='&&')

"""
output :: 
arj**
hunk&&angle

------------------

sep -- def is space (multiple values in the print stmnt)
end -- default is new line (multiple print stmnts)
"""
name = 'arjun'
age = 45
print(f'name is {name} and age is {age}')

print('hello {0} and this is {1} and ur into {2}'.format('arjun','sai','place'))

name = 'sai'
age = 43
color = 'white'

print('hello u r name is {n} and age is {a} and color ur taking is {c}'.format(n=name,a=age,c=color))

"""
formattted string - %.2f
"""

"""
Flow control :::

1. selection statements - if else
2. transfer statements - break and continue
3. iterative statements - for while

no ---- switch dowhile

pass del return

break and continue only in loops
"""

# loop with else block

"""
- loop with out break than only else block executes
"""
# pass is the placeholder / empty block

def funt():
    pass

strn = 'ABCDEFBKI'

print(strn.find('B'))
print(strn.rfind('B')) # reverse backward search

print(strn.find('FB',3,8))
print(strn.index('B',3,8))
print(strn.rindex('B',3,8))

"""
index - if the string is not available it gives error

find - gives '-1'
"""

print(strn.strip())

strn = 'ABCDEFBKI'
print(strn.count('ABC'))
print(strn.count('ABC', 1, 100))
print(strn.replace('ABC', 'FYI'))
"""
1
0
FYIDEFBKI
"""

# replace - casesensitive

# immutable - every change in string creates a new Obj

strn = 'string,for split'

# split

print(strn.split(','))  # default separator = space

# return type == list

# join

exm = ['this', 'beauty', 'healthy']

print('-'.join(exm))


strn = 'Example for capital string and Some more letters on it'

print('Uppercase: ',strn.upper())

print('Lower: ',strn.lower())

print('Swap Case: ',strn.swapcase())

print('Title:',strn.title())

print('Capitalize:',strn.capitalize())


"""
Uppercase:  EXAMPLE FOR CAPITAL STRING AND SOME MORE LETTERS ON IT
Lower:  example for capital string and some more letters on it    
Swap Case:  eXAMPLE FOR CAPITAL STRING AND sOME MORE LETTERS ON IT
Title: Example For Capital String And Some More Letters On It     
Capitalize: Example for capital string and some more letters on it
"""
# reversed function and slice
name = 'arjun'
print(name[::-1])
rev = reversed(name)
out = "".join(rev)
print(out)
# without any method reverse of the string
name = 'arjun'
out = ''
i = len(name)-1
while i>=0:
    out=out+name[i]
    i = i -1
print(out)


## LIST

l = []
l.append(10)
l.append('sai')
l.append('hi')
l.append(10)

print(l)

"""
- insertion order preserved
- duplicate values allowed
- hetrogenous obj r allowed
- list is dynamic , we can add and remove
- list is mutable
- []

list()

"""

# new = eval(input('enter:'))

# print(new)

list1 = [10,20,30]
list2 = [50,60]

print(list1+list2) ## both should be list (type error)

print(list2 * 3) # list and int

# relational operator list

"""
- number of elements must be same
- order of elements must be same
- content must be same including case

"""

animal = ['Dog','Cat','Lion']
animal2 = ['dog','Cat',]
animal3 = ['dog','Cat','Lion']

print(animal==animal2)
print(animal==animal3)
print(animal2==animal3)

"""
comparision operator - <,>,<=

number of elements are not important. it compares each item wise
"""

l = [10,20,30]

l1 = [10,50]

print(l<l1)

# membership operators - in

meml1 = [10,20,30,40]

print(10 in meml1)
# if the value is there in the list returns true
meml1 = [10,20,30,40]
print(10 in meml1)

l = [10,20,30]

# python inbuilt functions which are genric to every data type
print(len(l)) # length



# list specific methods

l.append(12)

print(l)
print(l.count(10))  # count method

print(l.index(10)) # returns index of first presence

# adding elements into list

l = [10,20]

l1 = (40,50)

l.append(30) # adds at the end of list
l.insert(2,34) # adds at the specific index , takes 2 arguments

l.extend(l1) # adds an iterative object into list

l.append(l1) # adds object at the end....
print(l) # [10, 20, 34, 30, 40, 50, (40, 50)]

"""
del keyword

s1='durga'
s2=s1
s3=s2

del s2,s3

-- eligible for GC

slice operator ---> no index out of range exeception

s[9:0:0] ---> value error

math operators for string:

+ concatenation ( str + str

* repititation ( int * str

'a' in 'arjun'

in and not in operators

comparision operators:

'durga' > 'ravi'  ==== like to like comparision

ord('d')

find rfind
index rindex
strip
count
replace

split
join

upper()
lower()
swapcase()
title()
capitalize()

---------------

s.startswith(substr)

s.endswith(substr)

s.isalnum()

s.isalpha

s.islower

s.isupper

s.isdigit()

s.istitle()

s.isspace()

# List

insertion order is preserved and duplicates allowed


- insertion order
- duplicate objects
- hetrogenous objects r allowed
- dynamic , add and remove
- mutable
- []
---> 


list()



"""

# remove items from list

# remove - to remove specified


l = [10,20,30,40,20]

l.remove(50) # ValueError: list.remove(x): x not in list

l.remove(20) # only the first element

print(l)

# list pop

l = [10, 20, 30]
l.pop()

print(l)  # last item

# if pop method is used on empty list - index error

poplist = [10, 20, 4, 5]

poplist.pop(3)  # remove the element at specified index
print(poplist)

print(l.pop())  # index out of range if not there i the list

# remove vs pop

# clear()

clearlist = [1,2,3,5]

clearlist.clear()

print(clearlist)
# reverse method

l.reverse()

"""
revers vs reversed

- reverese existing list only changes happens
- list specfic method
- none return type

reverese -
generic function
creates new object

"""

sortlist = [10,20,30]

sortlist.sort(reverse=True) # desc

# items must be homogenous

"""default sort num - ascending
               string - alphabetical
               """

"""
sort vs sorted 

- sorted creates a new list obj
"""


# alaising and cloning

newl = [10,20,30]
new3 = newl[::]
new2 = newl.copy()
print(id(newl),id(new2))


# list comprehension

l = [x for x in range(10)]

print(l)

l = [x*x for x in range(1,10) if x%2==0 ]

print(l)

## tuple

# immutable, ()







