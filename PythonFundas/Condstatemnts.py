if True:
    pass    # pass statement is used as placeholder.

lang = 'Java'

if lang == 'Python':
    print(lang)
else:
    print('some other lang..')

if lang == 'Python':
    print(lang)
elif lang == 'Java':
    print('java lang')
else:
    print('not lang..')


# and or not

user = 'admin'
logged_in = True

if user == 'admin' and logged_in: ## and - both should be True, OR --> one should be True
    print('get in')
else:
    print('Invalid')

## is - 2 objets with same id..

a = [1.2]
b = a

print(a is b) # True 

"""

::Evalutes to false::

False None 
() ,  '' , []
{}


"""
