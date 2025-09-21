from person import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        self.__gpa = 0.0  

    def enroll_course(self, course):
        self.course_list.append(course)

    def show_courses(self):
        return f"Enrolled courses: {', '.join(self.course_list)}" if self.course_list else "No courses enrolled."

  
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0 and 4.0")

    @staticmethod
    def is_valid_id(student_id):
        return student_id.startswith("S-")
