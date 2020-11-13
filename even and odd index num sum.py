
# even and odd index num sum 

list1 = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
List=len(list1)
odd = 0
even  = 0
for i in range(List): 
	if i % 2 == 0:
		even += list1[i]
	else:
		odd += list1[i] 
print ("Even index positions sum ", even) 
print ("Odd index positions sum ", odd )
    


