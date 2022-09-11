"""
scope = The region that a variable is recognised.
        A variable is only available from inside the region it is created.
        A global and locally scoped versions of a variable can be created
"""

name = "MT" # This variable ha sa global scope, it is available both within and outside a variable

def display_name(): # The name variables scope is restricted to the defined function, this is a local variable
    name = "Michael"
    print(name)


display_name()
