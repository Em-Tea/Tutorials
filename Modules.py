# import converters - this imports the entire module rather than the methods we need
import utils
from utils import lbs_to_kg # Here, we import only what we need from another module.
from utils import find_max
# print(converters.lbs_to_kg(100))
print(lbs_to_kg(100))

input_list = list(map(int, input("Please enter a list of numbers: ").split(' ')))
"""
In the block of code above, we prompt an input from the user which we intend to store as a list 
- input() this function always returns a string
We use the string method .split and pass in a space to split the contents of the input into separate values 
next our map function iterates through each individual value and performs int() casting
Finally, the list() assigns each integer to an index within a list, this makes it ready for use. 
"""
print(input_list)
print(find_max(input_list))
