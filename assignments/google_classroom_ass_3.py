def rev(a):
    list1 = []
    for word in a:
        list1.append(word[-1: : -1])
    return list1
main = ["abc", "tuv", "xyz"]
print(rev(main))
