# list

name = ['ani','bob','khan','joy']

print("negative index : ",name[-1])

print('index : ',name[2])
print('length func : ',len(name))

print('slicing list : ',name[0:2]) # start is inclusive and last is exclusive

#gives the items from 0 index to 2 , not including 2


name.append('root')

print('append function : ',name) # appends at end

name.insert(0,'aniket')

print('insert at spec index : ',name)

# extend

list1 = [1,2,3]

list2 = [4,5]

list1.extend(list2)

print('extend the list : ',list1)


name.remove('aniket')

print('removed item', name)

name.pop()

print('pops out last item', name)

nums = [1,2,3]

nums.reverse()
print("reverse of numbers",nums)

nums.sort(reverse=True)
print("sort numbers descending",nums)

nums.sort()
print("sort in desc",nums) # ascending

sorted_list = sorted(nums)

print('sorted list', sorted_list)

print("min of numbers :",min(nums))

print("max of numbers :",max(nums))

print('index of : ', name.index('joy')) # if its not there will get value error

## enumerate

lis = [1,2,3]

for index,i in enumerate(lis,start=1):
    print("enumerate list : ",index,i)


## string to list

animals = ['cat','dog','lion','fox']

new_string = " - ".join(animals)

print('join string : ',new_string)  # cat - dog - lion - fox

list_string = new_string.split(' - ')
print('list string : ',list_string) # ['cat', 'dog', 'lion', 'fox']


####  OUTPUT #####

"""
negative index :  joy
index :  khan
length func :  4
slicing list :  ['ani', 'bob']
append function :  ['ani', 'bob', 'khan', 'joy', 'root']
insert at spec index :  ['aniket', 'ani', 'bob', 'khan', 'joy', 'root']
extend the list :  [1, 2, 3, 4, 5]
removed item ['ani', 'bob', 'khan', 'joy', 'root']
pops out last item ['ani', 'bob', 'khan', 'joy']
reverse of numbers [3, 2, 1]
sort numbers descending [3, 2, 1]
sort in desc [1, 2, 3]
sorted list [1, 2, 3]
min of numbers : 1
max of numbers : 3
index of :  3
enumerate list :  1 1
enumerate list :  2 2
enumerate list :  3 3
join string :  cat - dog - lion - fox
list string :  ['cat', 'dog', 'lion', 'fox']

"""
