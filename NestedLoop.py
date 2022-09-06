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

print("")

newnums = [3, 6, 2, 8, 4, 10]
max = newnums[0]
for n in newnums:
    if n > max:
        max = n
print(max)

print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

print("")

extranums = [5, 2, 1, 7, 4]
extranums.insert(0, 10)
extranums.append(20)
extranums.pop()
print(extranums.index(1)) # checking values index
print(50 in extranums) # quick check
print(extranums)
print(extranums.count(2))
extranums.sort()
print(extranums)
extranums.reverse()
print(extranums)
extraextranums = extranums.copy()
extraextranums.pop()
print(extraextranums)
print("")

dupenums = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in dupenums:
    if number not in uniques:
        uniques.append(number)
print(dupenums)
print(uniques)