from student import Student
from teacher import Teacher
from person import Person

def display_role(person):
    if isinstance(person, Student):
        return f"{person.name} is a Student."
    elif isinstance(person, Teacher):
        return f"{person.name} is a Teacher."
    elif isinstance(person, Person):
        return f"{person.name} is a Person."
