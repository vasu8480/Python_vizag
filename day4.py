# ---------------- Swap 2 Numbers (without 3rd variable) ----------------

x, y = 44, 15

# Method 1: Using addition/subtraction
x = x + y
y = x - y
x = x - y
print(x, y)   # swapped values


# Method 2: Using multiplication/division
# NOTE: gives float due to division
x = x * y
y = x / y
x = x / y
print(x, y)   # float output


# Method 3: Using XOR (bitwise)
x = int(x)
y = int(y)

x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)   # swapped values


# Method 4: Pythonic way (recommended)
x, y = y, x
print(x, y)


# ---------------- Sum of Digits ----------------

# Method 1: Using while loop
n = 123
sum_val = 0

while n > 0:
    d = n % 10        # get last digit
    sum_val += d      # add to sum
    n = n // 10       # remove last digit

print(sum_val)   # 6


# Method 2: Using string
num = "1456"
su = 0

for i in num:
    su += int(i)   # convert char → int

print(su)   # 16


# ---------------- Count Occurrence (example: vowels/char) ----------------
str1 = "vasu is a good a00 boy"
str2 = "a"

c = 0
for i in str1:
    if i == str2:
        c += 1

print(c)                 # manual count
print(str1.count("a"))   # built-in method


# ---------------- Palindrome ----------------

# Method 1: Using reverse()
s = "madam"

string = list(s)     # convert to list
string.reverse()     # reverse list
rev = "".join(string)

print(rev)

if s == rev:
    print('pali')
else:
    print("not pali")


# Method 2: Using loop
s = "madam"
rev = ""

for i in s:
    rev = i + rev   # build reverse string

if rev == s:
    print('pali')
else:
    print("not pali")


# Method 3 (best): slicing
s = "madam"

if s == s[::-1]:
    print("pali")
else:
    print("not pali")
