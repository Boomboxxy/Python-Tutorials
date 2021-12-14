# fromkeys :
# d = {'name' : 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name','age'],'unknown') # list
# d = dict.fromkeys(('name','age'),'unknown') # tuple
# d = dict.fromkeys('abc','unknown') # string -----> {'a' : 'unknown','b' : 'unknown','c' : 'unknown'}
# d = dict.fromkeys(range(1,11),'none') # range
# d = dict.fromkeys(('name','age'),[1,2,3,4]) # we can store any thing
# print(d)

# GET METHOD :
d = {'name' : 'kaustubh', 'age' : 24}

# common method to access the dictionaries :
# print(d['name']) # no error
# print(d['names']) # error

# using the get method :
# print(d.get('name')) # no error
# print(d.get('names')) # none

# common method :
if 'name' in d :
    print('exists')
else :
    print('not exists')

# using get method :
if d.get('name'):
    print('exists')
else :
    print('not exists')

# if None ----> false,   else ----> true

# clear method :
# d.clear() # empty the dictionary
# print(d)

# copy method :
d1 = d.copy()
print(d1)
