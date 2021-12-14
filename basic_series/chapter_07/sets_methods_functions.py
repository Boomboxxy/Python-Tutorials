# set methods:
s = {1,2,3,4}
# add():
# s.add(5,6,7,8) # error
# add() only takes 1 argument
s.add(5)
s.add(6)
s.add(7)
s.add(8)
s.add(9)
print(s)

# clear():
# s.clear()
# print(s)

# remove():
# s.remove(6)
# s.remove(10) # error
# print(s)
#    _or_
s.discard(6)
s.discard(10)# no error
print(s)

# copy():
s1 = s.copy()
print(s1)
print(s)
