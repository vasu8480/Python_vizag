# ---------------- Conditional Append ----------------
l = [1,2,3,4]
a = []

for i in range(len(l)):
    # if index is even → append value*2, else do nothing
    msg = a.append(l[i]*2) if i % 2 == 0 else 0

print(a)  # [2, 6]

# NOTE: Better version (add else case)
# a.append(l[i]) if i%2==0 else a.append(l[i])


# ---------------- List / Set / Dict Comprehension ----------------
l1 = [1,2,3,4]
print([i*2 for i in l1 if i % 2 == 0])  # [4, 8]

l2 = [5,6,7,8]
print({i*2 for i in l2 if i % 2 == 0})     # {12,16} (set)
print({i: i*2 for i in l2 if i % 2 == 0})  # {6:12, 8:16} (dict)


# ---------------- Find Duplicates ----------------
char = ['a','b','c','d','e','a','f','b']
dup = []

for i in char:
    if char.count(i) > 1:
        dup.append(i)

print(dup)  # duplicates (repeated)


# remove duplicate entries in result
dup = []
for i in char:
    if char.count(i) > 1:
        if i not in dup:
            dup.append(i)

print(dup)  # ['a','b']


# ---------------- Max Even Number ----------------
l = [1,2,3,4,5,6,7,8,9,10]

print(max([i for i in l if i % 2 == 0]))  # 10


def max_even(l):
    ma = []
    for i in l:
        if i % 2 == 0:
            ma.append(i)
    return max(ma)

print(max_even(l))


# ---------------- Factorial (Recursion) ----------------
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # 120


# ---------------- Prime Number ----------------
def prime(n):
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

print(prime(8))  # False (NOTE: your comment was wrong earlier)


# Another method
n = 1

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")


# ---------------- Prime in Interval ----------------
def prime_range(a, b):
    for i in range(a+1, b):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)

prime_range(1, 113)


# ---------------- Dictionaries ----------------
dic = {
    'a': 6,
    'b': 2
}
print(dic)
print(dic['a'])   # access value


# keys can be strings, numbers, tuples (immutable)
dic = {
    '123': [1,2,3],
    'b': "hello"
}
print(dic)


# duplicate keys → last one overrides
dic = {
    "123": (1,2,3),
    "123": 'hello'
}
print(dic)   # only last value kept


# ---------------- Dictionary Methods ----------------
user = {
    'name': 'vasu',
    'age': 24
}

print(user)
print(user.get('name'))  # safe access

print('vasu' in user)    # False (checks keys only)
print('name' in user)    # True

print(user.values())     # values
print('vasu' in user.values())  # True

print(user.items())      # key-value pairs


# ---------------- Copy vs Clear ----------------
user2 = user.copy()   # copy

print(user2)

print(user.clear())   # clears original
print(user)           # {}
print(user2)          # still has data


# ---------------- Pop Operations ----------------
# NOTE: user is empty now → below will error if used

# print(user.pop('name')) → KeyError if key not present
# print(user.popitem()) → removes last inserted item


# ---------------- Loop Through Dictionary ----------------
user = {
    'name': 'vasu',
    'age': 24,
    'city': 'vizag'
}

for i in user:
    print(i)   # keys

for i in user.values():
    print(i)   # values

for i in user.keys():
    print(i)   # keys

for k, v in user.items():
    print(k, v)   # key-value pairs


# ---------------- Prime Check (final snippet) ----------------
n = 1

# 1 is not prime
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")
