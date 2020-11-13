# arms num or not.py

arms_num=int(input("enter any num1:"))
digit_number=int(input("anter any num2:"))
i=1
sum=0
while i<=0:
	digit_number=arms_num%digit_number
	print(digit_number)
	sum=sum+digit_number
if sum==digit_number:
	print("it is arms_num:")
else:
	print("it is not arms_num:")
