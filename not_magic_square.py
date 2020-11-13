# not_magic_square.py

magic= [
    [5, 3, 7],
    [1, 8, 9],
    [6, 4, 2]
]
a=0
c=0
d=0
dia=2
sum1=0
sum2=0
for i in range(3):
	row=(sum(magic[a]))
	a+=1
	di1=((magic[c][d]))
	sum1+=di1
	di2=(magic[c][dia])
	sum2+=di2
	dia-=1
	c+=1
	d+=1
	b=0
	diag2=(sum2)
	diag1=(sum1)
	for j in range(3):
		b+=magic[j][i]
	col=(b)
	b+=1
if diag1==diag2==row==col:
	print('it is magic square')
else:
	print('it is not magic square')


