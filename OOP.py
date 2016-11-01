class SchoolMember:
    """ represents any school member"""

    def __init__(self, name, age):
        self.name = name
        self.stream = age
        print("Initialized SchoolMember: {})".format(self.name))

    def tell(self):
        """Tell my details"""
        print('Name: "{}" Age: "{}"'.format(self.name, self.stream), end=" ")


class Teacher(SchoolMember):
    """Represents a teacher"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    """Represents a student"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Miss. Clare', 35, 32000)
s = Student('Andy', 19, 84)
# print a blank line
print()

members = [t, s]
for members in members:
    # works for both teachers and students
    members.tell()
