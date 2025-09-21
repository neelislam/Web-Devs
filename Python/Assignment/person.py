class Person:
    total_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old."

    @classmethod
    def get_total_people(cls):
        return cls.total_people
