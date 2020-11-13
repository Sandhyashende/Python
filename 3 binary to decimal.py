# 3 binary to decimal:

b_num =['1', '0', '0', '1', '1', '0', '1', '1']
value = 0
i=0
while i<len(b_num):
	num = b_num.pop()
	if num == '1':
		value = value + pow(2, i)
	i = i + 1
print(value)
