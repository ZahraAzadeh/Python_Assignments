class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# 🧑‍💻 Get student data from user
name = input("Enter the student's name: ")

try:
    grade_input = input("Enter grades separated by commas (e.g., 85,90,78): ")
    grades = [float(g.strip()) for g in grade_input.split(",")]

    student = Student(name, grades)
    average = student.calculate_average()

    print(f"{student.name}'s average grade is: {average:.2f}")

except ValueError:
    print("Error: Please enter valid numeric grades separated by commas.")
