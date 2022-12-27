'''
num = 153
sum = 0
o=len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** o
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#if else elif example
def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(find_max(10,20,30))

##leap year
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
print(leap_year(2000))

#factors of a number
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
factors(10)

# #power of without using power function
a,b=2,3
power=b
res=1
for b in range(b,0,-1):
    res=res*a
print(res)

while b!=0:
    res=res*a
    b-=1
print(res)

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
print(power(2,3))



a=(1,2,3,4,5,6,4,78)
print(a.index(4))

#len of string without using len function
a="vasu"
count=0
for i in a:
    count+=1
print(count)

#len of list without using len function
count=0
for i in b:
    count+=1
print(count)



# #max of list without using max function
max=0
for i in b:
    if i>max:
        max=i
print(max)

# #min of list without using min function
min=0
for i in b:
    if i<min:
        min=i
print(min)


# #reverse of string without using reverse function
rev=""
for i in a:
    rev=i+rev
print(rev)

# #reverse of list without using reverse function
rev=[]
for i in b:
    rev.insert(0,i)
print(rev)


# c=(1,2,3,4,5,6,4,78)
#reverse of tuple without using reverse function
rev=()
for i in c:
    rev=(i,)+rev
print(rev)


#enumerate is used to iterate over a list and get the index and value of each item in the list
# 0 v
# 1 a
# 2 s
# 3 u
a="vasu"
for i in enumerate(a):
    print(i)
for i,k in enumerate(a):
    print(i,k)

# 0 5
# 1 8
# 2 42
# 3 698
# 4 4
b=[5,8,42,698,4]
for i,k in enumerate(b):
    print(i,k)


from functools import reduce
#lambda
f = lambda x: x*x
print(f(5)) # 25

#map is used to apply a function to each item in a list
def square(x):
    return x*x
print(list(map(square, [1,2,3,4,5]))) # [1, 4, 9, 16, 25]
print(list(map(lambda x:x*x, [1,2,3,4,5]))) # [1, 4, 9, 16, 25]

#filter is used to filter out the elements from a list based on a condition
def is_odd(x):
    return x%2 == 1
print(list(filter(lambda x:x%2, [1,2,3,4,5]))) # [1, 3, 5]

#reduce is used to apply a function to a list and reduce it to a single value
def add(x,y):
    return x+y
print(reduce(lambda x,y:x+y, l)) 
print(reduce(add, [1,2,3,4,5])) # 15
print(reduce(add, [1,2,3,4,5], 10)) # 25


#sorted
print(sorted([1,2,3,4,5], reverse=True)) # [5, 4, 3, 2, 1]
print(sorted([1, 2, 3, 4, 5], key=lambda x: x % 2)) #[2, 4, 1, 3, 5]
print(sorted([1, 2, 3, 4, 5], key=lambda x: x % 2, reverse=True))  #[1, 3, 5, 2, 4]

#sorted
print(sorted(["abc","adb", 'Zoo', 'Credit'], key=str.lower)) # ['abc', 'adb', 'Credit', 'Zoo']
#everse 
print(sorted(["adc","acb", 'Zoo', 'Credit'], key=str.lower, reverse=True)) # ['Zoo', 'Credit', 'adc', 'acb']



l=[1,2,3]
l2=[6,7,8,9,10]
#multiply 
print(list(map(lambda x,y:x*y,l,l2)))  # [6, 14, 24]

#odd numbers
print(list(filter(lambda x:x%2==1,l))) # [1, 3]

#multiply every value by 2
print(list(map(lambda x:x*2,l))) # [2, 4, 6]

#multiply every value by 2
print([i*2 for i in l]) # [2, 4, 6]

#multiplication of all values in a list
print(reduce(lambda x,y:x*y,l)) # 6

#mutiplied by all numbers and again multiplied by 2
print(reduce(lambda x,y:x*y,l,2)) # 12

#sum of all numbers
print(reduce(lambda x,y:x+y,l)) # 6

#sum of all numbers with first number
print(reduce(lambda x,y:x+y,l,2)) # 8

#regular expression
import re
s = '123ab8c456def789ghi'
#findall()
print (re.findall('\d+',s)) # ['123', '8', '456', '789']

#finditer()
for i in re.finditer('\d+',s): # 123 8 456 789
    print( i.group())

#search()
m = re.search('\d+',s) # 123
print (m.group()) 

#match()
n = re.match('\d+',s) # 123
print (n.group())

#split()
print (re.split('\d+',s)) # ['', 'ab', 'c', 'def', 'ghi']

#sub()
print (re.sub('\d+','*',s)) # *ab*c*def*ghi

#compile()
p = re.compile('\d+') # 123 8 456 789
print (p.findall(s))
'''