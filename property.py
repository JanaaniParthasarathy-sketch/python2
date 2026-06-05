class Student:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value

s = Student()
s.marks = 95
print(s.marks)
