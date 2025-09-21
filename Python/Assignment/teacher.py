from person import Person

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def introduce(self):
        return f"I am Professor {self.name}, teaching {self.subject}."
