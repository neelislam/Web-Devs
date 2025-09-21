from student import Student

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    def show_thesis(self):
        return f"My thesis title is: {self.thesis_title}"
