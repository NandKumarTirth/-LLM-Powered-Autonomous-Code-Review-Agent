class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


def display_student(student):
    print(f"Name: {student.name}")
    print(f"Average Marks: {student.calculate_average()}")


def generate_report(students):

    total_students = len(students)

    averages = []

    for student in students:
        averages.append(student.calculate_average())

    highest = max(averages)
    lowest = min(averages)

    print("===== REPORT =====")
    print("Total Students:", total_students)
    print("Highest Average:", highest)
    print("Lowest Average:", lowest)

    for student in students:
        print(student.name, student.calculate_average())

    print("Report Generated Successfully")


students = [
    Student("Nand", [80, 85, 90]),
    Student("Rahul", [70, 75, 80]),
    Student("Amit", [90, 92, 95])
]

for student in students:
    display_student(student)

generate_report(students)