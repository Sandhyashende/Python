# sum_of_even_odd.py

list1 = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
List=len(list1)
odd = 0
even  = 0
for i in range(List): 
	if i % 2 == 0:
		even += list1[i]
	else:
		odd += list1[i] 
print ("sum of even num:",even) 
print ("sum of odd num:",odd)
