for x in range(4):
    print("Outer loop control")
    for y in range(3):
        print("Inner loop control")
        print(f'X = {x}, Y = {y}')

print("----------------------------")

numbers = [6, 2, 6, 2, 2]
for num in numbers:
    print("x" * num)

print("")

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print("")

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
count = 0
print(names[0:2]) # specify a range of index with a colon

newnums = [3, 6, 2, 8, 4, 10]
max = newnums[0]
for n in newnums:
    if n > max:
        max = n
print(max)



