#  4 binary to decimal:

b_num = ['1','1','0','0','1','0','1','1']
print(b_num)
i = 0
value = 0
while i <(len(b_num)):
	num = b_num.pop()
	if num == '1':
		value = value + pow(2, i)
		i= i +1
print(value)