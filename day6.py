'''
l=[1,2,3,4]
a=[]
for i in range(len(l)):
    msg= a.append(l[i]*2) if i%2==0 else 0
print(a) # [2, 6]
#question  else ----> a.append(l[i])

l1=[1,2,3,4]
print([i*2 for i in l1 if i%2==0]) # [4, 8]

l2=[5,6,7,8]
print({i*2 for i in l2 if i%2==0}) # {16,12}
print({i:i*2 for i in l2 if i%2==0}) # {6: 12, 8: 16}


char=['a','b','c','d','e',"a","f","b"]
dup=[]
for i in char:
    if char.count(i)>1:
        dup.append(i)
print(dup) # ['a', 'b', 'a', 'b']

char=['a','b','c','d','e',"a","f","b"]
dup=[]
for i in char:
    if char.count(i)>1:
        if i not in dup:
            dup.append(i)
print(dup) # ['a', 'b']

max even number
l=[1,2,3,4,5,6,7,8,9,10]
print(max([i for i in l if i%2==0])) # 10
def max_even(l):
    ma=[]
    for i in l:
        if i%2==0:
            ma.append(i)
    return max(ma)
print(max_even(l)) # 10

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5)) # 120

prime number
def prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
print(prime(8)) # True

prime 
n=1
if n>1:
		for i in range(2,n):
				if n%i==0:
						print("not prime")
						break
		else:
				print("prime")
else:
		print("not prime")
Prime interval

def prime(a,b):
    for i in range(a+1,b):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
prime(1,113)

dic={
    'a':6,
    'b':2
}
print(dic)
print(dic['a'])

dic={
    '123':6,
    'b':2
}
print(dic)

dic={
    '123':[1,2,3],
    'b':"hello",
}
print(dic)
dic={
    "123":(1,2,3),
    "123":'hello',
   # [100,200,300]:'hello' # TypeError: unhashable type: 'list'
}
print(dic)

user={
    'name':'vasu',
    'age':24
}
print(user) # {'name': 'vasu', 'age': 24}
print(user.get('name')) # vasu
print('vasu' in user) # False
print('name' in user)   # True
print(user.values()) # dict_values(['vasu', 24])
print('vasu' in user.values()) # True  
print(user.items()) # dict_items([('name', 'vasu'), ('age', 24)])

user2=user.copy()
print(user2) # {'name': 'vasu', 'age': 24}
print(user.clear())
print(user) # {}
print(user2) # {'name': 'vasu', 'age': 24}

print(user.pop('name')) # vasu
print(user) # {'age': 24}

print(user.popitem())  # randomly removes one item


user={
    'name':'vasu',
    'age':24,
    "city":"vizag"
}
for i in user:
    print(i) # name age city
for i in user.values():
    print(i) # vasu 24 vizag
for i in user.keys():
    print(i) # name age city
for k,v in user.items():
    print(k,v) # name vasu age 24 city vizag
'''

#prime number
n=1
