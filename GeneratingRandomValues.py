import random
import Classes

for i in range(5):  # We use a for loop to denote how many times we'd like to iterate and produce the code block
    print(random.randint(10, 20))  # Here we use the randomint() method, two parameters are required to specify a range.

print("")

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)
print("")
dice = Classes.Dice()
print(f'You rolled the dice...{dice.roll()}')

