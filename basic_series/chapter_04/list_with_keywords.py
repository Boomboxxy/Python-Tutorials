entertainment = ['books', 'tv', 'computer', 'outside']

select = input('Name an entertainment option : ')
if select in entertainment:
    print(f'{select} is an entertainment option.')
elif select not in entertainment:
    print(f'{select} is not an entertainment option.')