class University():  # PARENT CLASS / SUPERCLASS
    def __init__(self, n, i):
        print("\n A new object is created")
        self.name = n
        self.id = i

    def getID(self):
        return self.id

    def firstName(self):
        fname, lname = self.name.split()
        return fname

    def fullName(self):
        return self.name


class Employee(University):  # CHILD CLASS
    def __init__(self, n, i, s, t):
        super().__init__(n, i)
        self.salary = s
        self.title = t

    def printAnnualSalary(self):
        print(self.name, "earns", self.salary * 12, "per year")

    def fullName(self):
        return (self.title + ". " + self.name)


class Student(University):  # Another CHILD CLASS
    def __init__(self, n, i, cl):
        super().__init__(n, i)
        self.courseList = cl

    def numCourses(self):
        x = len(self.courseList)
        return x


# MAIN Code
A = University("Albert Einstein", 1788)
print("A is an employee named", A.firstName())

B = University("Hareem Nisar", 1200)
print("B is a student with ID", B.getID())

C = Employee("Aysha Mansoor", 8597, 5000, "Prof")
print(C.firstName())
print(C.fullName())
C.printAnnualSalary()

D = Student("Mandeep", 11, ["Python", "Java", "C++"])
print(D.getID())
# D.printAnnualSalary #error
print("You are taking ", D.numCourses(), "courses")

E = University("John Doe", 1155)
print(E.fullName())

F = Employee("Majid Maqbool", 567, 5000, "Dr")
print(F.fullName())
