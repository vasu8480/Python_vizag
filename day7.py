'''
class Trainer:
    def __init__(self):
        self.name = "vasu"
        self.location = "avanthi"
        self.rank = 1
# Object instantiation
c=Trainer()
print(c.name)
print(c.location)
print(c.rank)

class Trainer:
    name = "vasu"
    def __init__(self):
        self.college = "avanthi"
 

avanthi = Trainer()
print("{} is a Trainer".format(avanthi.__class__.name))

#acessing class variable
print("Trainer name: ", Trainer.name)

#changing the class variable
Trainer.name = "ravi"

# Accessing class attribute
print("{} is a Trainer".format(avanthi.__class__.name))

# Accessing instance attributes
print("Trainer name: ", Trainer.name)


#oops
class Trainer:
    def __init__(self):
        self.name = "vasu"
        self.location = "avanthi"
        self.rank = 1
    def ava(self):
        return f"{self.name} is studying in  {self.location} and has a rank of {self.rank}"
p=Trainer()
print(p.ava())
print(Trainer().ava())

#both down are same
class Trainer:
    def __init__(self,name, college, rank):
        self.name = name
        self.location = college
        self.rank = rank
    def ava(self):
        return f"{self.name} is studying in  {self.location} and has a rank of {self.rank}"
print(Trainer("vasu", "avanthi", 1))
print(Trainer("vasu", "avanthi", 1).ava())


class Trainer:
    def __init__(self,name, college, rank):
        self.name = name
        self.location = college
        self.rank = rank
    def __str__(self):
        return f"{self.name} is studying in  {self.location} and has a rank of {self.rank}"
print(Trainer("vasu", "avanthi", 1))

#same college
class Trainer:
    def __init__(self,name, college, rank):
        self.name = name
        self.college = college
        self.rank = rank
    def compare(self, other):
        if self.college == other.college:
            return "same college"
        else:
            return "different college"
    def __str__(self):
        return f"{self.name} is studying in  {self.college} and has a rank of {self.rank}"

c=Trainer("vasu", "avanthi", 12)
c1=Trainer("ravi", "avanthi", 16)
print(c.compare(c1))

class Trainer:
    name = "vasu"
    def __init__(self):
        self.college = "avanthi"

    @classmethod
    def gettrainer(cls):
        return cls.name
        
    @staticmethod
    def info():
        return "this is a trainer"
    
avanthi = Trainer()
print(Trainer.gettrainer())
print(Trainer.info())




#inheritance
class college:
    def __init__(self,name, college, rank):
        self.name = name
        self.location = college
        self.rank = rank
    def __str__(self):
        return f"{self.name} is studying in  {self.location} and has a rank of {self.rank}"

class student(college):
    def __init__(self, name, college, rank):
        super().__init__(name, college, rank)
        print("student details")
print(student("vasu", "avanthi", 1))



#multiple inheritance
class college:
    def __init__(self):
        self.name = "vasu"
        self.location = "avanthi"
    def __str__(self):
        return f"{self.name} is studying in  {self.location}"

class student():
    def __init__(self):
        self.rank = 1
        self.roll=19
        
class c(college,student):
    def __init__(self):
        super().__init__()
        print("student details")
print(c())

#user inputs
# a=list(map(int,input().split()))
# print(a)

# b=list(map(str,input().split()))
# print(b)
# f=input().split()
# print(f)

#how to take input from user
# a=int(input()) 
# print(a)
# b=input()
# print(b)


'''
