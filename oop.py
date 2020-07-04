class Student:
    def __init__(self):
        self.name = "Ralf"
        self.grade = (90, 100, 89, 98, 97)

    def average(self):
        return sum(self.grade) / len(self.grade)


student = Student()

print(student.average())



