# Loop Control Statements = change a loops execution from its normal sequence

# break = used to terminate the loop
# continue = skips to the next iteration of the loop.
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

pnum = "123-456-7890"
for i in pnum:
    if i == "-":
        continue
    print(i, end="")

