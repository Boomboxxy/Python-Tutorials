# in keyword & looping in dictionaries

user_info = dict(
    name = 'kaustubh',
    age = 12,
    fav_movies = ['abc1','abc2','abc3'],
    fav_tunes = ['xyz1','xyz2','xyz3']
)

# check if key exists in the dictionary
# if 'name' in user_info :
#     print('present')
# else :
#     print('not present')

# check if value exists in the dictionary
# if 12 in user_info.values() :
#     print('present')
# else :
#     print('not present')

# if ['abc1','abc2','abc3'] in user_info.values() :
#     print('present')
# else :
#     print('not present')

# loops in dictionaries :

    # to print the keys :
# for i in user_info :
    # print(i)

    # to print the values :
# for i in user_info.values() :
    # print(i)

# items method :
user_items = user_info.items()
print(user_items)
print(type(user_items))
# returns the key and value pair in the form of a tuple.
# <class 'dict_items'> = type of the user_items
# output ----> ([(key : value),(key : value),(key : value),(key : value)])
