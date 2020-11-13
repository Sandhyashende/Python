# count_char_list.py

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
p=0
i=0
n=0
t=0
x=0
u=0
g=0
while i <len(char_list):
	if "a" in char_list[i]:
		p+=1
	elif "n" in char_list[i]:
		n+=1
	elif "t" in char_list[i]:
		t+=1
	elif "x" in char_list[i]:
		x+=1
	elif "u" in char_list[i]:
		u+=1
	elif "g" in char_list[i]:
		g+=1
	i=i+1
print("a-",p,"times")
print("n-",n,"times")
print("t-",t,"times")
print("x-",x,"times")
print("u-",u,"times")
print("g-",g,"times")