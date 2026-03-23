# ---------------- Formulas (just notes) ----------------
# area of circle = pi * r**2
# area of rectangle = l * w
# volume of sphere = (4/3) * pi * r^3


# ---------------- String Formatting ----------------
name = 'vasu'
age = '24'

print(f'hi {name} you are {age}')  
# f-string → hi vasu you are 24

print('hi {} you are {}'.format('vasu', 25))  
# format() → hi vasu you are 25

print('hi {1} you are {0}'.format('vasu', 25))  
# positional format → hi 25 you are vasu


# ---------------- String Slicing ----------------
# syntax: str[start:stop:step]
a = 'hi all avanthi'

print(a[0:5])     # hi al (0 to 4 index)
print(a[1:5])     # i al
print(a[1:-1])    # i all avanth (exclude last char)
print(a[1:-1:2])  # ialavn (step 2)
print(a[1:-1:3])  # iaai (step 3)


# ---------------- String Immutability ----------------
# a[0] = "8" → ERROR (strings are immutable)
# cannot modify string directly


# ---------------- String Length ----------------
l = len("vasu")
print(l)  # 4


# ---------------- String Methods ----------------
a = 'vasu'
print(a.upper())  # VASU

a = "VasU"
print(a.lower())  # vasu

a = "vasui"
print(a.find("as"))       # 1 (index of substring)
print(a.replace("u", "k"))  # vaski


# ---------------- Split ----------------
a = 'Python Programming'

print(a.split(' '))  # ['Python', 'Programming']
print(a.split('o'))  # split on 'o'
print(a.split('P'))  # split on 'P'


# ---------------- Reverse / Negative Index ----------------
print(a[-1:])        # last character
print(a[-1::-1])     # reverse string
print(a[-4:-1])      # substring
print(a[-1:-3:-1])   # reverse slicing


# ---------------- Password Masking ----------------
username = "vasu"
passwd = "vasu10"

pass_len = len(passwd)
hid_pas = '*' * pass_len   # create hidden password

print(f'your password {hid_pas} is {pass_len}')


# ---------------- Lists ----------------
# properties:
# mutable, ordered, indexed, iterable

l = [1,2,3,4,5,6,7]
l2 = ['hi','all','how','are','you']

cart = ['pen','pencil','laptop']

cart[0] = "scale"   # update element
print(cart)

cart.extend(l2)     # add list items
print(cart)

cart.extend('vasu') # adds each char
print(cart)


# ---------------- List Operations ----------------
# print(cart.pop())  # removes last element

print(cart)

print(cart.remove('pen'))  # remove by value (returns None)
print(cart)

# del cart → deletes entire list
# print(cart) → ERROR (list no longer exists)


# ---------------- List Utilities ----------------
print("laptop" in cart)     # membership check
print(cart.count('pen'))    # count occurrences

print(cart.sort())   # sorts in-place, returns None
print(cart)

print(sorted(cart))  # returns new sorted list
print(cart)          # original unchanged

cart.reverse()       # reverse in-place
print(cart)


# ---------------- Join ----------------
print(" ".join(cart))  # join list into string


# ---------------- Loops ----------------
for i in cart:
    print(i)   # print each element

for i in a:
    print(i)   # iterate string

for i in "hi all":
    print(i)


# ---------------- Range ----------------
a = [1,2,3,4,5,6,7,8,9,10]

for i in a:
    print(i)

print(range(1,100))        # range object
print(list(range(1,100)))  # convert to list

for i in range(0,50):
    print(i)   # 0 to 49


# incorrect loop (won’t run because step is negative but start < end)
for _ in range(0,10,-1):
    print(_)

for _ in range(10,0,-1):
    print(_)   # 10 to 1


# ---------------- While Loop ----------------
# infinite loop (no increment)
# i = 0
# while i < 10:
#     print(i)

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("done")  # executes after loop completes


# ---------------- Move Zeros (Method 1 - Not Recommended) ----------------
# modifying list while iterating → unsafe

a = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0]
print(a)

for i in a:
    if i == 0:
        a.remove(i)  # remove zero
        a.append(i)  # add at end

print(a)


# ---------------- Move Zeros (Method 2 - Better) ----------------
a = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0]

l = []

for i in a:
    if i != 0:
        l.append(i)   # add non-zero elements

# add remaining zeros
for i in range(len(a) - len(l)):
    l.append(0)

print(l)
