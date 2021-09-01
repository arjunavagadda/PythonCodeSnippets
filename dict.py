
# Dictionary

student = {
    'name': 'arjun',
    'age': 18,
    'courses': ['Maths','Computers','Arts']
}  # keys can be any immutable items

print(student['courses'][0]) # Maths

print(student.get('class','Not found')) # if the ket is not found returns the default - None / if we sepcify the arg. it returns that

student['name'] = 'john' # replaces the original value

student.update({}) # takes dict as arg. , we can update multiple items in the dict

print(student)

del student['age'] # removes the age item

namevar = student.pop('name')

print('namevar',namevar) # john

##  dict - key and values

emp = {
    'id': 'mary',
    'rank': 23,
    'desig': 'dev'
}

print('keys',emp.keys()) # keys dict_keys(['id', 'rank', 'desig'])

print('values',emp.values()) # keys dict_values(['mary', 23, 'dev'])

print('key - value', emp.items()) # key - value dict_items([('id', 'mary'), ('rank', 23), ('desig', 'dev')])

# looping through dict......

for key,val in emp.items():
    print(key,val)
