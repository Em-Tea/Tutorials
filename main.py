# We can use formatted strings to clean up code
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)

# We create two placeholders within our string and insert variable names to fill these gaps using {}
msg = f'{first} [{last}] is a coder'
print(msg)
# the result is a cleaner and more legible form of presenting the same code and output
