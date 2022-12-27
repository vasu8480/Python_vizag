'''
#Polymorphism
#Polymorphism is the ability to take on many forms. 
# The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

def poly(a,b):
    return a+b
print(poly(2,3))
print(poly("vasu","avanthi"))

#duck typing
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
    def explain(self,understand):
        understand.teach()
t=Trainer()
teacher=reg_class()
vasu=crt_class()
t.explain(teacher)
t.explain(vasu)


# Encapsulation
# Encapsulation is the process of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
# In Python, we denote private attributes using underscore as the prefix i.e single “ _ “ or double “ __ “.
# Single _ underscore is used to denote protected attributes and methods.
# Double __ underscore is used to denote private attributes and methods.

class encapsulation:
    def __init__(self):
        self._name = "vasu"
        self.__college = "avanthi"
class student(encapsulation):
    def __init__(self):
        encapsulation.__init__()
        print(self._name)
        print(self.__college)
print(encapsulation())  # encapsulation  object
print(encapsulation()._name) # encapsulation object

#abstarction
#Abstraction is the process of hiding the implementation details from the user, only the functionality will be provided to the user.
# In Python, we can achieve abstraction by using abstract classes and interfaces.
# Abstract class: An abstract class is a class that contains one or more abstract methods.
# An abstract method is a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod
class Abstraction(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def display(self):
        pass
class student(Abstraction):
    def __init__(self, name):
        Abstraction.__init__(self, name)
    def display(self):
        print(self.name)
s = student("vasu")
s.display()

def factorial(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact
print(factorial(5))


#fibonacci
# Program to print the fibonacci series upto n_terms

# Recursive function
def recursive_fibonacci(n):
	if n <= 1:
		return n
	else:
		return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2)) # 8

n_terms = 6
print(recursive_fibonacci(n_terms))
# check if the number of terms is valid
for i in range(n_terms):
	print(recursive_fibonacci(i))

def fun(*args):
    return sum(args)
print(fun(1,2,3,4,5,6,7,8,9,10))

def fun(*args,**kwargs):
    total=0
    for i in kwargs.values():
        total+=i
    return sum(args)+total
print(fun(1,2,3,4,5,6,7,8,9,10,a=1,b=2))




'''