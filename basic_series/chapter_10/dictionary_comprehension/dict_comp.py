# square = {1 : 1, 2 : 4, 3 : 9, .... 10 : 100}
dictionary = {}
for i in range(1,11):
    dictionary[i] = i * i
#print(dictionary)

new = {}

#print({i:i*i for i in range(1,11)})

string = "andres rod."
# {"a" : 1, "n": 1, "d" : 2, ...}


#print({i:string.count(i) for i in string})

#{1:odd, 2:even, 3:odd, 4:even, .....20:even}


print({i:"odd" if i % 2 != 0 else "even" for i in range(1,21)})
