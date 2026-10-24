class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks >= 97:
            return "A"
        elif self.marks >= 78:
            return "B"
        elif self.marks >= 80:
            return "C"
        return "Pass"
