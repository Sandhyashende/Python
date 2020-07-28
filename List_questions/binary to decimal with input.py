# question7: binary to decimal with input


b_num = list(input("Input a binary number: "))
print(b_num)
value = 0
for i in range(len(b_num)):
	num = b_num.pop()
	if num == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)
