# question4:second max element

list_nums = [50,40,23,70,56,12,5,10,7]
minimum =int()
max,min = minimum, minimum
for num in list_nums:
    if num > max:
        max, min = num, max
    elif max > num > min:
        min = num
print(min if min != minimum else None)
