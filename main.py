# We can use formatted strings to clean up code

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)

# We create two placeholders within our string and insert variable names to fill these gaps using {}
msg = f'{first} [{last}] is a coder'
print(msg)
# the result is a cleaner and more legible form of presenting the same code and output

while True:
    exampleInput = input("Please enter your username: ")
    if len(exampleInput) > 25 or len(exampleInput) < 4:
        print("Character limit is 4 to 25")
    else:
        print(f'{exampleInput}, Thank you for signing up to our service')
        break

house_Price = 1000000
print("Please enter your credit score below")
creditscore = input()
creditscore = int(creditscore)
if creditscore > 700:
    print(f'Congratulations! You qualify for a 10% down payment of £{house_Price * 0.1}')
else:
    print(f'You qualify for a 20% down payment of £{house_Price * 0.2}')

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')

i = 1
while i <= 5:
    print('I' * i)
    i += 1
print("Done")