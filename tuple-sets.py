
# tuple

"""
- immutable

"""

stu_Set = ('dog','ant')

# sets

batsman_player = {'sachin','kohli','dhoni','irfan'}

bowl = {'bumrah','khan','munaf','irfan'}

print(batsman_player.intersection(bowl)) # {'irfan'}

print(batsman_player.difference(bowl)) # {'sachin', 'kohli', 'dhoni'}

print(batsman_player.union(bowl)) # {'irfan', 'dhoni', 'bumrah', 'kohli', 'khan', 'sachin', 'munaf'}

se ={1,2,3}

st = {4,5,6}

print(se.intersection(st)) # set()

print('khan' in batsman_player) # sets are more preferred for 'in' operator


## empty objects

emptylist  = []
empty_list = list()

empty_tuple = tuple()
emptytu = ()

empty_Set = set()
emptyset = {} # this is not set its a <<dict>>>
