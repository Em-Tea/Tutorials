"""
Nested function called = function calls inside other function calls
                         innermost function calls are resolved first
                         returned value is used as an argument for the next outer function
"""


"""num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)"""

print(round(abs(float(input("Enter a number")))))
# above, returned values are passed in as an argument for the next outer function
# input reads input and passed this to float, then to abs, then to round, and finally, the result is printed.
