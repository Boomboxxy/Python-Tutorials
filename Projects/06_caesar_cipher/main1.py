from resources import logo, alphabet, caps

print(logo)

either = input("Type 'encrypt ' to encrypt, type 'decode' to decode: ")
message = input('Type your message: ')
shift = int(input('Type the shift number: '))
new = ''

#The function that encrypts the letters
def add(letters,list1,move):
    pos = list1.index(letters)
    if pos + move > 25:
            a = (pos + move) - 25
            return list1[a - 1]
    else:
            return list1[pos + move]


#The function that decodes the letters
def sub(letters,list1,move):
    pos = list1.index(letters)
    if pos - move < 0:
        a = pos - shift
        return alphabet[a]
    else:
        return alphabet[pos - shift]

#The full encryption of the message
if either == 'encrypt':
    for letter in message:
        if letter in alphabet:
            new += add(letter,alphabet,shift)
        elif letter in caps: 
            new += add(letter,caps,shift)
        else:
            new += letter
#The full decoding of the message       
else:   
    for letter in message:
        if letter in alphabet:
            new += sub(letter,alphabet,shift)
        elif letter in caps: 
            new += sub(letter,caps,shift)
        else:
            new += letter

print(new)


