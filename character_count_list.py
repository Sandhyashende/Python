# character_count_list.py

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i <len(char_list):
      if char_list [i] not in  a:
            a.append(char_list[i])
      i=i+1
print(a)
j=0
b=[]
while j<len(a):
      k=0
      count=0
      c=[]
      while k<len(char_list):
            if a[j]==char_list[k]:
                  count=count+1
            k=k+1
      c.append(a[j])
      c.append(count)
      b.append(c)
      j=j+1
print(b)
      

