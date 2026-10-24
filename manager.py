class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            student.display()
            print("Grade:", student.grade())
            print("-" * 70)
