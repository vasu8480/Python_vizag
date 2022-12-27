'''
#question
# are of circle=p*r**2
# area rect=l*w
# volume of sphere =(4/3)*pi*r*r*r

name='vasu'
age='24'
print(f'hi{name} you are {age}') #hi vasu you are 24
print('hi{} you are {}'.format('vasu',25)) # hi vasu you are 25
print('hi{1} you are {0}'.format('vasu',25)) #hi25 you are vasu

#str=[start:stop:stepover]
a='hi all avanthi'
print(a[0:5]) #hi all
print(a[1:5]) #i al
print(a[1:-1]) #i all avanthi
print(a[1:-1:2]) #ialavn
print(a[1:-1:3]) #iaai


a[0]="8"
print(a)    #immutable

l=len("vasu")
print(l)

a='vasu'
print(a.upper()) #VASU
a="VasU"
print(a.lower()) #vasu

a="vasui"
print(a.find("as")) #1
print(a.replace("u","k")) #vaski

a='Python Programming'
print(a.split(' ')) #['Python', 'Programming']
print(a.split('o')) #['Pyth', 'n Pr', 'gramming']
print(a.split('P')) #['Python ', 'rogramming']


print(a[-1:])
print(a[-1::-1])		#step index
print(a[-4:-1])			#rev
print(a[-1:-3:-1])

#question
username="vasu"	
passwd="vasu10"
pass_len=len(passwd)
hid_pas='*'*pass_len
print(f'you password {hid_pas} is {pass_len}')

#Lists
#list examples 
#list is a collection of items
#list is mutable
#list is ordered
#list is indexed
#list is iterable
l=[1,2,3,4,5,6,7]
l2=['hi','all','how','are','you']

cart=['pen','pencil','laptop']
cart[0]="scale"
print(cart)
cart.extend(l2)

print(cart)
cart.extend('vasu') #extend each char as a list 
print(cart)

# print(cart.pop())
print(cart)

print(cart.remove('pen')) #remove by value
print(cart)

del cart	#removes the cart
print(cart)

print("laptop" in cart)
print(cart.count('pen'))  #1 count of pen

print(cart.sort())
print(cart)

print(sorted(cart)) #sorted list but not change the original list 
print(cart)

print(cart)
cart.reverse() #reverse the list but not change the original list
print(cart)

sen=" "
print(" ".join(cart)) #join the list with space and print as a string
for i in cart:
		    print(i) #print each element in the list 


for i in a:
	print(i) #print each char in the string

for i in "hi all":
	print(i)

a=[1,2,3,4,5,6,7,8,9,10] #list
for i in a: 
	print(i) #print each element in the list

print(range(1,100))
print(list(range(1,100)))

for i in range(0,50):
	print(i) #print 0 to 49

for _ in range(0,10,-1):
	print(_) #print 0 to 9

for _ in range(10,0,-1):
	print(_) #print 10 to 1

i=0				#infinte loop
while i<10:
	print(i) 

i=0
while i<10:
	print(i)  #print 0 to 9
	i+=1
else:print("done") #print done after 10


# move zeros to the end of the list
#-----------------------------------method 1-----------------------------------

a=[1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0]
print(a)
for i in a:
	if i==0:
		a.remove(i)
		a.append(i)
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]
end = time.time()
print(end - start)
  
#-----------------------------------method 2-----------------------------------
a=[1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0]
l=[]
for i in a:
	if i!=0:
		l.append(i)
for i in range(len(a)-len(l)):
	l.append(0)
print(l) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''