class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

    def __len__(self):
        return 10

class Cat(Animal):

    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class something(object):
    """docstring for something"""
    def run(self):
        print("something can't move.")

def run_twice(animal):
    animal.run()
    animal.run()

heimi = Dog()
print(type(heimi))

run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(something())
print("=======================")
print(len(heimi))


print("===================================>")

class MyObjection(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x*self.x

obj = MyObjection()
setattr(obj,'y',20)
print(obj.y)
setattr(obj,'x',10)
print(obj.power())
fn = getattr(obj,'power')
print(fn())