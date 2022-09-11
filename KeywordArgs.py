"""
Keyword arguments = arguments preceded by an identifier when we pass them to a function.
                    the order of the args does not matter, unlike positional arguments.
                    Python knows the names of the arguments that our function recieves.
"""


def hi(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hi("Taylor", "Michael", "Terry")
hi(last="Taylor", first="Michael", middle="Terry")  # keyword arguments give us more control over passing in args.
