names = "kaustubh,albert,jad,andres,simone,soham,aboyami,martijn,george, what"

list = []
i = ''
for v in names:
    if v == ',':
        list.append(i)
        i = ''
    else:
        i += v
if v:
    list.append(v)
print(list)