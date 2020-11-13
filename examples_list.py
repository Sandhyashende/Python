
# examples_list.py

names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print (names_list[0]) # se "annu" print hoga
print (names_list[4] )# se "rupa" print hoga
names_list[0] = "abhishek"
print(names_list)
names_list[3]="rishabh"
print (names_list)
names_list[4]="dhruv"
print(names_list)
names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print (len(names_list))
print (names_list)
names_list.append("dhruv")
print ("length of the list is ", len(names_list))
print (names_list)
names_list.append("alok")
print ("length of the list is ", len(names_list))
print (names_list)
names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
names_list.pop()
print("length of the list is ", len(names_list))
print(names_list)
names_list.pop()
print ("length of the list is ", len(names_list))
print (names_list)
print ("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print ("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print ("length of the list is ", len(names_list), names_list)
"shivam" in names_list
"imtiyaz" in names_list
if "imtiyaz" in names_list:
	print ("imteyaj ka naam `names_list` mei hai")
else:
	print ("imteyaj ka naam `names_list` mei nahi hai")

