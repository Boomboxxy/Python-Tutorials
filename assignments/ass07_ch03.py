number = int(input('Which number\'s table do you want : '))
full = int(input('How large do you want the table : '))
# def num_table(a):
#     multy_by = 0
#     multy = 0
#     for i in range(1,11):
#         multy_by += 1
#         multy += 1
#         total = multy * a
#         print(f'{a} x {i} = {total}')
        

# num_table(table)


def table(number):
    for i in range(1,(full + 1)):
        print(f"{number} x {i} = {number*i}")

table(number)
