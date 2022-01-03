"""
Single Responsibility Principle

A class should have only one job.  If a class has more than one responsibility,
it becomes coupled.  A change to one responsibility results to modification of
the other responsibility.
"""

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
