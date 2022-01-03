'''
Open Closed Principle was first conceptualized by Berterd Meyer in 1988. Robert C. Martin mentioned this as “the most important principle of object-oriented design”.

Open Closed Principle states that “Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.”
'''


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'Bark'


class Mouse(Animal):
    def make_sound(self):
        return 'Meow'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animals = [
    Animal('Dog'),
    Animal('Cat'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'Dog':
            print('Bark')
        elif animal.name == 'Cat':
            print('Meow')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)
