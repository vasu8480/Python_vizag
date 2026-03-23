# ---------------- List Unpacking ----------------
# a, b, c, d, *others = [1,2,3,4,5,54,64,5,6]
# first 4 values go to a,b,c,d and rest go into 'others' as list


# ---------------- Input Handling ----------------
a = list(map(int, input().split()))
# takes space-separated input and converts to list of integers
print(a)


# ---------------- For Loop ----------------
for i in range(0, 50):
    print(i)   # prints 0 to 49


# ---------------- While Loop ----------------
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("done")  # executes after loop completes


# ---------------- Loop Control Statements ----------------
# continue → skip current iteration
# break → exit loop
# pass → do nothing (placeholder)

for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    print(i)

for i in range(1, 11):
    if i == 5:
        break   # stop loop at 5
    print(i)

for i in range(1, 11):
    if i == 5:
        pass   # does nothing


# ---------------- Multiplication Table ----------------
n = 5
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)


# ---------------- Pattern using Matrix ----------------
pic = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for i in pic:
    for j in i:
        if j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")   # move to next line


# ---------------- Square Pattern ----------------
for i in range(0, 5):
    for j in range(0, 5):
        print("*", end="")
    print()   # new line after each row


# ---------------- Triangle Pattern using List ----------------
myList = []

for i in range(1, 6):
    myList.append("*" * i)   # create pattern line

print(myList)                # ['*', '**', '***', ...]
print(type(myList))          # list

print("\n".join(myList))     # print pattern line by line
print(type("\n".join(myList)))  # string


# ---------------- Join with Numbers ----------------
l1 = [1,2,3,4,5,6,7,8,9,10]
print(" ".join(list(map(str, l1))))  
# convert int → str then join


l1 = ["1","2","3","4","5"]

print(" ".join(str(l1)))  
# wrong usage → joins characters of string representation

print(" ".join(str(i) for i in l1))  
# correct → joins elements


# ---------------- Right-Aligned Triangle ----------------
for row in range(1, 5):
    print(" " * (5 - row - 1) + "*" * row)


# ---------------- Number Pattern ----------------
b = 5

for i in range(6, 0, -1):
    b += 1
    for j in range(0, i):
        print(b, end=' ')
    print()


# ---------------- Reverse Star Pattern ----------------
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# ---------------- Collections ----------------
import collections

# Counter → count frequency of elements
a = dict(collections.Counter(['a','b','c','d','a','c']))
print(a)   # {'a':2, 'b':1, 'c':2, 'd':1}


# Deque → fast append/pop from both ends
dq = collections.deque([1,2,3,4,5,6,7])

dq.append(100)   # add to right end
dq.popleft()     # remove from left end

print(dq)
