def list(*args):
# Will return the first letter of each argument as a capital with the rest being loewrcase
#
    new_list = []
    for word in args:
        temp = word
        uppercase = temp[0].upper()
        lowercase = temp[1:].lower()
        new = uppercase + lowercase
        new_list.append(new)
    return new_list


print(list('pizza','pie'))
