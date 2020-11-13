# all_in_one_math_list.py

list1 = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
List1=len(list1)
odd = 0
even  = 0
count_even = 0
count_odd = 0
for i in range(List1): 
    if i % 2 == 0:
        even += list1[i]
        count_even+=1
    else:
        odd += list1[i] 
        count_odd+=1
    sum =count_even+count_odd
    sum2 =even+odd
average_1=even//count_even
average_2=odd//count_odd
average_3=sum2//sum
print ("element of even num in list: ", count_even,)
print("element of odd num in list:",count_odd)
print("total sum of even and odd element",sum)
print ("sum of even num:",even) 
print ("sum of odd num:",odd)
print("total sum of even and odd mun:",sum2)
print ("average of even num:",average_1) 
print ("average of odd num:",average_2)
print("total average of element",average_3)
print ("Odd index positions sum ", odd,count_odd,average_2)

