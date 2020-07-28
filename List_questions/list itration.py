question2: list itration 

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
list_length = len(numbers)
index = 0
less_than40 = 0
more_than20 = 0
while index < list_length:
	number = numbers[index]
	if number < 40:
		less_than40 = less_than40 + 1
	else:
		more_than20 = more_than20 + 1
	index = index + 1
print("total number more than 20:" + str(more_than20))
print("total number less than 40:" + str(less_than40))
