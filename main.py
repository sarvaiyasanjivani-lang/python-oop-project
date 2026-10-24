from student import Student
from manager import StudentManager

manager = StudentManager()

manager.add_student(Student("Sanjivani", 87))
manager.add_student(Student("Khushi", 77))
manager.add_student(Student("Vishwa", 94))

manager.show_students()
