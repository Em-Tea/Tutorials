class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("Walk")


class Dog(Mammal):
    def self(self):
        print("bark")


class Cat(Mammal):
    def be_adorable(self):
        print(f'{self.name} thinks that cats are the best')


cat1 = Cat("Jeremy")
cat1.be_adorable()
