
user_info = dict(
    name = 'kaustubh',
    age = 12,
    fav_movies = ['abc1','abc2','abc3'],
    fav_cricketers = ['xyz1','xyz2','xyz3']
)

# add data :
# user_info['fav_football_players'] = ['pqr1','pqr2','pqr3']
# print(user_info)

# pop method :
# popped = user_info.pop('fav_movies')
# print(popped)
# print(user_info)

# popitem method :
popped = user_info.popitem()# pops the last key : value pair
print(popped)
print(user_info)
