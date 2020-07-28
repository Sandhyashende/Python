# question12: find total sum

list_1= [10, 11, 12, 13, 14, 17, 18, 19]
list_2=[]
j=[-1]
for i in list_1:
    for j in list_1:
        num=[i,j]
        if i+j==30:
            list_2.append(num)
print(list_2[0:3])