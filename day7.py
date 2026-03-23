# ---------------- Basic Class & Object ----------------
class Trainer:
    def __init__(self):
        self.name = "vasu"        # instance variable
        self.location = "avanthi"
        self.rank = 1

# Object creation (instantiation)
c = Trainer()
print(c.name)
print(c.location)
print(c.rank)


# ---------------- Class Variable vs Instance Variable ----------------
class Trainer:
    name = "vasu"   # class variable (shared across all objects)

    def __init__(self):
        self.college = "avanthi"   # instance variable (unique per object)

avanthi = Trainer()

# accessing class variable using class reference
print("{} is a Trainer".format(avanthi.__class__.name))

print("Trainer name:", Trainer.name)

# modifying class variable
Trainer.name = "ravi"

print("{} is a Trainer".format(avanthi.__class__.name))
print("Trainer name:", Trainer.name)


# ---------------- Methods in Class ----------------
class Trainer:
    def __init__(self):
        self.name = "vasu"
        self.location = "avanthi"
        self.rank = 1

    def ava(self):   # instance method
        return f"{self.name} is studying in {self.location} and has rank {self.rank}"

p = Trainer()
print(p.ava())           # using object
print(Trainer().ava())   # direct object creation


# ---------------- Constructor with Parameters ----------------
class Trainer:
    def __init__(self, name, college, rank):
        self.name = name
        self.location = college
        self.rank = rank

    def ava(self):
        return f"{self.name} is studying in {self.location} and has rank {self.rank}"

print(Trainer("vasu", "avanthi", 1))       # prints object reference
print(Trainer("vasu", "avanthi", 1).ava()) # actual output


# ---------------- __str__ Method ----------------
class Trainer:
    def __init__(self, name, college, rank):
        self.name = name
        self.location = college
        self.rank = rank

    def __str__(self):
        # controls print(object)
        return f"{self.name} is studying in {self.location} and has rank {self.rank}"

print(Trainer("vasu", "avanthi", 1))


# ---------------- Compare Two Objects ----------------
class Trainer:
    def __init__(self, name, college, rank):
        self.name = name
        self.college = college
        self.rank = rank

    def compare(self, other):
        # compare two objects
        if self.college == other.college:
            return "same college"
        else:
            return "different college"

    def __str__(self):
        return f"{self.name} is studying in {self.college} and has rank {self.rank}"

c = Trainer("vasu", "avanthi", 12)
c1 = Trainer("ravi", "avanthi", 16)

print(c.compare(c1))


# ---------------- Class Method & Static Method ----------------
class Trainer:
    name = "vasu"

    def __init__(self):
        self.college = "avanthi"

    @classmethod
    def gettrainer(cls):
        # works with class variables
        return cls.name

    @staticmethod
    def info():
        # no access to class/instance variables
        return "this is a trainer"

avanthi = Trainer()

print(Trainer.gettrainer())
print(Trainer.info())


# ---------------- Inheritance ----------------
class College:
    def __init__(self, name, college, rank):
        self.name = name
        self.location = college
        self.rank = rank

    def __str__(self):
        return f"{self.name} is studying in {self.location} and has rank {self.rank}"


class Student(College):
    def __init__(self, name, college, rank):
        super().__init__(name, college, rank)  # call parent constructor
        print("student details")

print(Student("vasu", "avanthi", 1))


# ---------------- Multiple Inheritance ----------------
class College:
    def __init__(self):
        self.name = "vasu"
        self.location = "avanthi"

    def __str__(self):
        return f"{self.name} is studying in {self.location}"


class Student:
    def __init__(self):
        self.rank = 1
        self.roll = 19


class C(College, Student):
    def __init__(self):
        super().__init__()   # calls first parent (College)
        print("student details")

print(C())


# ---------------- User Input Examples ----------------
# a = list(map(int, input().split()))  # list of integers
# b = list(map(str, input().split()))  # list of strings
# f = input().split()                 # default string split

# a = int(input())   # integer input
# b = input()        # string input
