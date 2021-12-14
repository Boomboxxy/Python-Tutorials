amount = int(input('Insert how many numbers you want in the list : '))
list = []
"""
i = 1
while i < amount + 1:
    list.append(input(f'Insert number {i} : '))
    i += 1
print(f"Here's your list : {list}")
"""

for i in range(amount):
    list.append(int(input(f'insert number {i + 1} : ')))
print(f"Here's your list : {list}")