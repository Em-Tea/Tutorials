my_intlist = [2, 4, 6, 8, 10]
my_strlist = ["Hi,", "how", "are", "you"]

for n in range(1, 6):
    print(n)
print("-------------------------")

total = 0
prices = [23.99, 12, 7.99]
for price in prices:
    total += price
    print(f'£{total:.2f}')  #string format to show only 2 places
print(f'Your final total is: £{total}')
print("-----------------------")