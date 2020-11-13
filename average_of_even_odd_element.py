# average_of_even_odd_element.py

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
average_1=even//count_even
average_2=odd//count_odd
print ("average of even num:",average_1) 
print ("average of odd num:",average_2)

