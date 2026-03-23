# ---------------- Functions Basics ----------------

# parameters → variables in function definition
def say_hello():
    print('Hello')

say_hello()


def hello(name, emoji):
    print(f'Hello {name} {emoji}')

# arguments → values passed during function call
hello('vasu', '😀')   # positional arguments
hello("😎", "vasu")   # order matters


# ---------------- Default Arguments ----------------
def hello(name='vasu', emoji='😀'):
    print(f'Hello {name} {emoji}')

hello()   # uses default values


# ---------------- Keyword Arguments ----------------
hello(emoji='😎', name='vasu')  
# order doesn’t matter when using keywords


# ---------------- Return Values ----------------
def power(x, y):
    return x ** y   # returns result

print(power(2, 3))   # 8

# if no return → function returns None


def sum_val(x, y):
    return x + y

print(sum_val(2, 3))


# ---------------- Nested Function ----------------
def sum_val(x, y):
    def another_func(a, b):
        return a + b
    return another_func(x, y)

print(sum_val(20, 65))


# ---------------- Docstring ----------------
def sum_val(x, y):
    """this function returns the sum of two numbers"""
    return x + y

print(sum_val.__doc__)   # access documentation


# ---------------- Even or Odd ----------------
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(5))   # False


# ---------------- Sum of Digits ----------------
def sum_of_digits(n):
    sum_val = 0
    while n > 0:
        sum_val += n % 10
        n = n // 10
    return sum_val

print(sum_of_digits(123))   # 6


# ---------------- Count Even and Odd Digits ----------------

# Method 1: while loop
def even_odd(n):
    even = 0
    odd = 0
    while n > 0:
        r = n % 10
        if r % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10
    return even, odd   # returns tuple

print(even_odd(123456789))


# Method 2: using for loop (string length)
def ev(n):
    eve = 0
    od = 0
    for i in range(len(str(n))):
        r = n % 10
        if r % 2 == 0:
            eve += 1
        else:
            od += 1
        n //= 10
    return eve, od

print(ev(123456789))


# ---------------- List Unpacking ----------------
a, b, c, d, *others = [1,2,3,4,5,54,64,5,6]
print(a, b, c, d, others)

a, b, *c, d = [1,2,3,4,5,54,64,5,6]
print(a, b, c, d)   # 'c' holds middle elements


# ---------------- Sets ----------------
# unordered, unique elements, no indexing

my_set = {1,2,3,4,5,6,7,8,9,10}
print(my_set)

my_set.add(100)   # add element
print(my_set)

set1 = {1,2,3,2,3,4,5,6,4}
print(set1)   # duplicates removed automatically

set1.remove(2)   # remove element (error if not present)
print(set1)

# print(set1[0]) → ERROR (no indexing in sets)

print(1 in set1)   # membership check

print(len(set1))   # size of set

print(min(set1))
print(max(set1))
print(sum(set1))


# ---------------- Copy vs Reference ----------------
k = set1        # reference (same object)
n = set1.copy() # new copy

set1.clear()    # removes all elements

print(set1)  # empty set
print(k)     # also empty (same reference)


# ---------------- Set Operations ----------------
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9,10}

print(s1.union(s2))          # combine all elements
print(s1.intersection(s2))   # common elements
print(s1.difference(s2))     # in s1 not in s2
print(s2.difference(s1))     # in s2 not in s1

s1.discard(1)   # removes if present (no error)
print(s1)

s1.difference_update(s2)   # modifies s1
print("diff", s1)

print(s1.issubset(s2))     # check subset
print(s1.issuperset(s2))   # check superset
print(s1.isdisjoint(s2))   # no common elements
