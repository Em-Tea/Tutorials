"""
*args = parameter that will pack all arguments into a tuple
useful so that a function can accept a varying amount of arguments
"""


def add(*args): # *(name) - it is the astrix which denotes the use of tuple args within a function
    sum = 0
    for i in args:  # since our arguments are packed and passed as a tuple, we iterate through each index for a sum
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))

"""
**kwargs = parameter that will pack all arguments into a directory
           useful so that functions can accept a varying amount of keyword arguments
"""


def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title ='Mr', first='Michael',middle='Terrence', last='Taylor')
