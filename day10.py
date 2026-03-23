# ---------------- Armstrong Number ----------------
num = 153
sum_val = 0

o = len(str(num))   # number of digits
temp = num

while temp > 0:
    digit = temp % 10
    sum_val += digit ** o   # power of digits
    temp //= 10

if num == sum_val:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# ---------------- Max of Three ----------------
def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(find_max(10, 20, 30))


# ---------------- Leap Year ----------------
def leap_year(year):
    # divisible by 4 and not by 100 OR divisible by 400
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(leap_year(2000))


# ---------------- Factors of a Number ----------------
def factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

factors(10)


# ---------------- Power without built-in ----------------
a, b = 2, 3

res = 1
for i in range(b):
    res *= a

print(res)


# recursive power
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

print(power(2, 3))


# ---------------- Tuple Index ----------------
a = (1,2,3,4,5,6,4,78)
print(a.index(4))   # first occurrence


# ---------------- Length without len() ----------------
a = "vasu"
count = 0

for i in a:
    count += 1

print(count)


# list length (fix: define b)
b = [1,2,3,4,5]
count = 0

for i in b:
    count += 1

print(count)


# ---------------- Max without max() ----------------
max_val = b[0]

for i in b:
    if i > max_val:
        max_val = i

print(max_val)


# ---------------- Min without min() ----------------
min_val = b[0]

for i in b:
    if i < min_val:
        min_val = i

print(min_val)


# ---------------- Reverse String ----------------
a = "vasu"
rev = ""

for i in a:
    rev = i + rev

print(rev)


# ---------------- Reverse List ----------------
b = [1,2,3,4]
rev = []

for i in b:
    rev.insert(0, i)

print(rev)


# ---------------- Reverse Tuple ----------------
c = (1,2,3,4,5,6,4,78)
rev = ()

for i in c:
    rev = (i,) + rev

print(rev)


# ---------------- Enumerate ----------------
a = "vasu"

for i in enumerate(a):
    print(i)   # (index, value)

for i, k in enumerate(a):
    print(i, k)


b = [5,8,42,698,4]

for i, k in enumerate(b):
    print(i, k)


# ---------------- Lambda / Map / Filter / Reduce ----------------
from functools import reduce

# lambda
f = lambda x: x * x
print(f(5))


# map
print(list(map(lambda x: x*x, [1,2,3,4,5])))


# filter
print(list(filter(lambda x: x % 2, [1,2,3,4,5])))


# reduce
print(reduce(lambda x, y: x + y, [1,2,3,4,5]))
print(reduce(lambda x, y: x + y, [1,2,3,4,5], 10))


# ---------------- Sorted ----------------
print(sorted([1,2,3,4,5], reverse=True))

# even first, odd later
print(sorted([1,2,3,4,5], key=lambda x: x % 2))

print(sorted([1,2,3,4,5], key=lambda x: x % 2, reverse=True))


# string sorting (case insensitive)
print(sorted(["abc","adb",'Zoo','Credit'], key=str.lower))

print(sorted(["adc","acb",'Zoo','Credit'], key=str.lower, reverse=True))


# ---------------- List Operations ----------------
l = [1,2,3]
l2 = [6,7,8,9,10]

# multiply two lists (pairwise)
print(list(map(lambda x, y: x*y, l, l2)))  # stops at shortest list


# odd numbers
print(list(filter(lambda x: x % 2 == 1, l)))


# multiply each element by 2
print(list(map(lambda x: x*2, l)))
print([i*2 for i in l])   # list comprehension


# multiplication of all elements
print(reduce(lambda x, y: x*y, l))

# with initial value
print(reduce(lambda x, y: x*y, l, 2))


# sum
print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: x+y, l, 2))


# ---------------- Regular Expressions ----------------
import re

s = '123ab8c456def789ghi'

# find all numbers
print(re.findall(r'\d+', s))


# iterator
for i in re.finditer(r'\d+', s):
    print(i.group())


# first match anywhere
m = re.search(r'\d+', s)
print(m.group())


# match from start only
n = re.match(r'\d+', s)
print(n.group())


# split by numbers
print(re.split(r'\d+', s))


# replace numbers with *
print(re.sub(r'\d+', '*', s))


# compiled pattern (reuse)
p = re.compile(r'\d+')
print(p.findall(s))
