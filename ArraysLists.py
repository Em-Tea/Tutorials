my_intlist = [2, 4, 6, 8, 10]
my_strlist = ["Hi,", "how", "are", "you"]

for n in range(1, 6):
    print(n)
print("-------------------------")

total = 0
prices = [23.99, 12, 7.99]
for price in prices:
    total += price
    print(f'£{total:.2f}')  # string format to show only 2 places
print(f'Your final total is: £{total}')

print("-----------------------")

# A tuple is a collection which is ordered and unchangable - we can think of this list as a constant
# Unlike arrays, tuples are denoted with parenthesis ()

num_tuple = (1, 2, 3)
# num_tuple[0] = 100 this reassignment cannot occur and will throw an exception
print(num_tuple)

# UNPACKING

coordinates = (1, 2, 3)

"""
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
"""
x, y, z = coordinates  # This line achieves the same outcome as the three above. Items are assigned based on i
print(x, y, z)

