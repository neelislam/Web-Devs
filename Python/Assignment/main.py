from person import Person
from student import Student
from teacher import Teacher
from graduate_student import GraduateStudent
from utils import display_role

if __name__ == "__main__":
    p1 = Person("Alice", 40)
    s1 = Student("Bob", 20, "S-101")
    t1 = Teacher("Dr. Smith", 50, "T-500", "Mathematics")
    g1 = GraduateStudent("Charlie", 24, "S-202", "AI in Healthcare")
    #introduce
    print(p1.introduce())
    print(s1.introduce())
    print(t1.introduce())

    #courses
    s1.enroll_course("Data Structures")
    s1.enroll_course("Algorithms")
    print(s1.show_courses())

    #gpa
    s1.gpa = 3.8
    print("GPA:", s1.gpa)

    #graduate
    print(g1.show_thesis())

    #poly
    print(display_role(p1))
    print(display_role(s1))
    print(display_role(t1))

    #static
    print("Valid ID?", Student.is_valid_id("S-202"))
    print("Valid ID?", Student.is_valid_id("202"))

    #class
    print("Total People:", Person.get_total_people())
