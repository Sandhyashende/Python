# binary to decimal without input

# part 2

binary = '10011011'
value = 0
i = 0
while i < len(binary):
    value <<= 1   
    value += (binary[i] == '1')
    i += 1
assert value == int(binary, 2)
print(value)