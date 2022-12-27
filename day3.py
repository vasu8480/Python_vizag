"""
# a,b,c,d,*others=[1,2,3,4,5,54,64,5,6]
# print(a,b,c,d,others)

a=list(map(int,input().split()))
print(a)

for i in range(0,50):
	print(i)

i=0
while i<10:
	print(i)
	i+=1
else:print("done")

continue  break  pass
for i in range(1,11):
	if i==5:
		continue
	print(i)

for i in range(1,11):
	if i==5:
		break
	print(i)

for i in range(1,11):
	if i==5:
		pass
#multplication table
n=5
for i in range(1,11):
	print(n,'x',i,'=',n*i) 

# 			*        
#     * * *      
#   * * * * *    
# * * * * * * *  
#       *        
#       *

pic=[
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
]

for i in pic:
	for j in i:
		if j==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print(" ")
# #patterns
'''
*
**   
***  
**** 
*****
'''
for i in range(0,5):
	for j in range(0,5):
		print("*",end="")
	print()

    # *****
    # *****
    # *****
    # *****
    # *****



myList = []
for i in range(1,5+1):
    myList.append("*"*i)
print(myList)
print(type(myList))
print("\n".join(myList))
print(type("\n".join(myList)))
print(myList)

l1=[1,2,3,4,5,6,7,8,9,10]
print(" ".join(list(map(str, l1))))



l1=["1","2","3","4","5"]
#.join() method
print(" ".join(str(l1)))
print(" ".join(str(i) for i in l1))


# 	  *
#    **
#   ***
#  ****
 
for row in range(1, 5):
    print(" " * (5 - row-1) + "*" * row)
		


# # reverse for loop from 5 to 0

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5



b = 5
for i in range(6, 0, -1):
    b += 1
    for j in range(0, i ):
        print(b, end=' ')
    print()

# * * * * *
# * * * *
# * * *
# * *
# *



for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# sum oƒ  natural numbers
# sum of digits
# occurence of specific character


import collections
a=dict(collections.Counter(['a','b','c','d','a','c']))
print(a)

dq=collections.deque([1,2,3,4,5,6,7])
dq.apppend(100)
dq.popleft()
print(dq)
"""