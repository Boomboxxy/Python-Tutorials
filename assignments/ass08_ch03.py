# Palindrome Tracker

# Insert a word : dad
# It is a palindrome
# Insert a word : albert
# It is not a palindrome


word = input('Insert a word : ')

def palindrome(a):
    bob = a[-1::-1]
    if a == bob:
        return('It is a palindrome')
    else:
        return('It is not a palindrome')

print(palindrome(word))
