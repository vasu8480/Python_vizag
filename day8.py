# ---------------- Polymorphism ----------------
# same function behaves differently based on input type

def poly(a, b):
    return a + b

print(poly(2, 3))                 # 5 (int addition)
print(poly("vasu", "avanthi"))   # string concatenation


# ---------------- Duck Typing ----------------
# object behavior matters, not its type

class reg_class:
    def teach(self):
        print("teach")
        print("end")

class crt_class:
    def teach(self):
        print("teach")
        print("train")
        print("explain")

class Trainer:
    def explain(self, understand):
        # expects object with teach() method
        understand.teach()

t = Trainer()
teacher = reg_class()
vasu = crt_class()

t.explain(teacher)   # works
t.explain(vasu)      # works


# ---------------- Encapsulation ----------------
# restrict direct access to variables

class encapsulation:
    def __init__(self):
        self._name = "vasu"        # protected (convention)
        self.__college = "avanthi" # private (name mangling)

class student(encapsulation):
    def __init__(self):
        super().__init__()   # correct way to call parent constructor
        print(self._name)    # accessible
        # print(self.__college) → ERROR (private)

# accessing
obj = encapsulation()
print(obj._name)   # accessible but not recommended

# print(obj.__college) → ERROR
# correct way (name mangling)
print(obj._encapsulation__college)


# ---------------- Abstraction ----------------
from abc import ABC, abstractmethod

class Abstraction(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass   # no implementation

class student(Abstraction):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(self.name)

s = student("vasu")
s.display()


# ---------------- Factorial (Iterative) ----------------
def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

print(factorial(5))   # 120


# ---------------- Fibonacci ----------------
# recursive (not efficient for large n)

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

n_terms = 6

print(recursive_fibonacci(n_terms))  # nth value

for i in range(n_terms):
    print(recursive_fibonacci(i))   # series


# ---------------- *args ----------------
def fun(*args):
    return sum(args)   # accepts multiple positional arguments

print(fun(1,2,3,4,5,6,7,8,9,10))


# ---------------- *args and **kwargs ----------------
def fun(*args, **kwargs):
    total = 0

    for i in kwargs.values():
        total += i   # sum keyword values

    return sum(args) + total

print(fun(1,2,3,4,5,6,7,8,9,10, a=1, b=2))
