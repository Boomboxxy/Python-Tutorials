def common(list1,list2):
    same = []
    for number in list1:
        if number in list2:
            same.append(number)
    return same
numbers1 = [1,2,5,8]
numbers2 = [1,2,7,6]
print(common(numbers1,numbers2))
