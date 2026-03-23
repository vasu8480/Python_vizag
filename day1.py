# ---------------- Arithmetic Operators ----------------
a = 132
b = 10

print(a + b)   # Addition -> 142
print(a - b)   # Subtraction -> 122
print(a * b)   # Multiplication -> 1320
print(a / b)   # Division (float) -> 13.2
print(a // b)  # Floor division (integer part) -> 13
print(a ** b)  # Power (132^10)
print(a % b)   # Modulus (remainder) -> 2


# ---------------- Assignment Operators ----------------
a = 10
b = 20

a += b   # a = a + b -> 30
print(a)

a -= b   # a = a - b -> 10
print(a)

a *= b   # a = a * b -> 200
print(a)

a /= b   # a = a / b -> 10.0
print(a)

a %= b   # a = a % b -> 10
print(a)


# ---------------- Comparison Operators ----------------
a = 10
b = 20

print(a > b)   # False -> 10 is not greater than 20
print(a < b)   # True  -> 10 is less than 20
print(a == b)  # False -> values are not equal
print(a != b)  # True  -> values are not equal
print(a >= b)  # False -> not greater or equal
print(a <= b)  # True  -> less or equal


# ---------------- Bitwise Operators ----------------
a = 8    # Binary: 1000
b = 20   # Binary: 10100

print(a & b)   # AND -> common bits
print(a | b)   # OR -> combine bits
print(a ^ b)   # XOR -> different bits
print(~a)      # NOT -> complement (-9)
print(~b)      # NOT -> complement (-21)
print(a >> 3)  # Right shift (divide by 2^3)
print(a << 2)  # Left shift (multiply by 2^2)


# ---------------- Logical Operators ----------------
a = 10
b = 20

print(a and b)  # Returns b (20) since both are True
print(a or b)   # Returns a (10) since first is True
print(not a)    # False (non-zero is True)
print(not b)    # False


# ---------------- Identity Operators ----------------
a = 10
b = 20

print(a is b)        # False -> different objects in memory
print(a is not b)    # True


# ---------------- String Print Examples ----------------
x = "Python"
y = "is"
z = "awesome"

print(x, y, z)                 # Print with spaces
print(x + " " + y + " " + z)   # String concatenation


# ---------------- If-Else Example ----------------
a = 10
b = 20

if a > b:
    print("a is greater")
else:
    print("b is greater")   # Executes because 20 > 10


# ---------------- If-Elif-Else Example ----------------
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")  # Executes
else:
    print("a is greater than b")
