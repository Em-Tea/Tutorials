# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print(f'The {animal} jumped over the {item}')
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))
print("The {animal} jumped over the {item}".format(animal="cat", item="sun"))

name = "MT"

print(f'Hello, my name is {name}.')
print("Hello, my name is {:10}. Nice to meet you".format(name))  # Adding padding to a value
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left alignment
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # right alignment
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # center alignment

num1 = 3.14159
num2 = 1000

print(f"The number pi is {num1}")
print("The number pi is {:.2f}".format(num1))
print("The number is {:,}".format(num2))  # Adding comma to place value
print("The number is {:b}".format(num2))  # binary format
print("The number is {:o}".format(num2))  # octal format
print("The number is {:X}".format(num2))  # hex format
print("The number is {:E}".format(num2))  # scientific notation
print(f'The number is {num2:.b}')
