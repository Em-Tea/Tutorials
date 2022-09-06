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
    if len(exampleInput) > 25:
        print("Character limit is 25")
    else:
        print(f'{exampleInput}, Thank you for signing up to our service')
        break
gcfhjgfhcj