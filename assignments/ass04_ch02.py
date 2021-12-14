fibbo = input('How many numbers do you want from the fibbonacci sequence?')
try:
    fibbo = int(fibbo) - 1
except:
     print('ERROR: Not a number')
     quit()


total = '0'

a = 0
b = 1
i = 0
v = 0
while i != fibbo:
    c = a + b
    v = c
    v = str(v)
    total += ' '
    total += v
    a = b
    b = c
    i += 1
    if i == fibbo:
        break

print(total)


