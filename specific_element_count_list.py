# specific_element_count_list.py

        
l = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
print(set([i for i in l if(l.count(i)>1)]))
