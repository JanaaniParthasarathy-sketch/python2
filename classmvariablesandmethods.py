#class variables
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Janaani")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)

#class methods
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")
print(Student.school)
