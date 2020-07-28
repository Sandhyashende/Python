#  list iteration

test_list1 =[23,67,90,45,56,78]
test_list2 = [10, 20, 56, 45, 36, 20]
print("The original list 1 is : " + str(test_list1)) 
print("The original list 2 is : " + str(test_list2)) 
print("The paired list contents are : ") 
for ele in test_list1 + test_list2: 
	print(ele, end =" ") 
