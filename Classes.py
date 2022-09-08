class Point:  # Pascal naming convention
    def __init__(self, x, y):  # Self references itself as an object
        self.x = x
        self.y = y

    def move(self):
        print("The point moves")

    def draw(self):
        print("Draw")

    def position(self):
        print(self.x, self.y)


point1 = Point(15, 30)
point1.position()


class Person:
    def __init__(self, name): # Constructor method
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}.')


person1 = Person("John Smith")
person1.talk()
