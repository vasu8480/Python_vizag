'''
#parameters are the variables in the function definition
def say_hello():
    print('Hello')
say_hello()

def hello(name,emoji):
    print(f'Hello {name} {emoji}')

#arguments are the values passed to the function when it is called
hello('vasu','😀')
#positional arguments
hello("😎","vasu")

#Default arguments
def hello(name='vasu',emoji='😀'):
    print(f'Hello {name} {emoji}')
hello()

#keyword arguments
hello(emoji='😎',name='vasu')

def power(x,y):
    return x**y    #what if not returned
print(power(2,3))

def sum(x,y):
    return x+y
print(sum(2,3))

def sum(x,y):
    def another_func(a,b):
        return a+b
    return another_func(x,y) 
print(sum(20,65))

""" 
it is used to explain what the function does
"""
def sum(x,y):
    """this function returns the sum of two numbers"""
    return x+y
print(sum.__doc__)
 
 #Even or odd
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(5))

#count sum of digits
def sum_of_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum
print(sum_of_digits(123))

#count no even digits and odd digits
#using for loop
def even_odd(n):
    even=0
    odd=0
    while n>0:
        r=n%10
        if r%2==0:
            even+=1
        else:
            odd+=1
        n=n//10
    return even,odd
print(even_odd(123456789))
#using while loop
def ev(n):
    eve=0
    od=0
    for i in range(0,len(str(n))):
        r=n%10
        if r%2==0:
            eve+=1
        else:
            od+=1
        n//=10
    return eve,od
print(ev(123456789))


a,b,c,d,*others=[1,2,3,4,5,54,64,5,6]
print(a,b,c,d,others)

a,b,*c,d=[1,2,3,4,5,54,64,5,6]
print(a,b,c,d,others)

my_set={1,2,3,4,5,6,7,8,9,10}
print(my_set)

my_set.add(100)
print(my_set)

set1={1,2,3,2,3,4,5,6,4}
print(set1)

set1.remove(2)
print(set1)

# print(set1[0])

print(1 in set1)

print(len(set1))

print(min(set1))
print(max(set1))
print(sum(set1))

k=set1
n=set1.copy()
set1.clear()
print(set1)
print(k)

s1={1,2,3,4,5}
s2={4,5,6,7,8,9,10}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
s1.discard(1)
print(s1)
s1.difference_update(s2)
print("diff",s1)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))

'''


