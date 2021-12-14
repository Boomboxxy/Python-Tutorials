# sets :

# unordered collection of unique elements
# they are declared using curly brackets
# sets are not dynamic
# we can only store integer, string, float data type
# we cannot store list or dictionaries in the sets
# we cannot use indexing in the sets
# sets are mostly used to remove duplicates

# eg. :
s = {1,2,3,4}

# to remove duplicate from a list :
l = [1,2,3,3,4,5,5,6,6,6,7,7,9,9,7,8,7,5]
convert = list(set(l)) # set function
print(convert)
