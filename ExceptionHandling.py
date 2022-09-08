bool = None
n = 6

if n < 5 and n > 3:
    print("a")
    bool = True
elif n >= 5 and n < 7:
    print("b")
    bool = False
print(bool)


while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0 and age <= 113:
            print(age)
            break
        else:
            print("Please enter a valid age")
    except ValueError:
        print("Please enter a number")


try:
    n = int(input(""))
    if n > 100 and n < 200:
        print("a")
    else:
        print("b")
except ValueError:
    print("invalid")