# even_odd_element.py

List1 = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even,odd = 0,0
for List in List1:
	if List%2==0:
		even+=1
	else:
		odd+=1
print("element of even num in list: ",even)
print("element of odd num in list: ",odd)

