# palindrome_true_false.py

name=["naina","anamana","sandhya","nitin"]
for i in name:
    _name=i[::-1]
    if i==_name:
        print(_name,">true")
    else:
        print(_name,"false")