# count_specific_element_list.py

list1 = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
a =[]
while i <len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]==list1[j]:
            b=list1[i]
            a.append(b)
            break
        j=j+1
    i=i+1
print(a)