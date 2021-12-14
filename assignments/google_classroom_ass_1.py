def sqr(numbers):
	squared = []
	for number in numbers:
		squared.append(number ** 2)
	return squared
list = [1,2,3,4]
print(sqr(list))