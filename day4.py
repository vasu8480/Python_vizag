'''
#Swap 2 numbers without 3 variables
			x,y=44,15
			x=x+y
			y=x-y
			x=x-y
			print(x,y)

			x=x*y
			y=x/y
			x=x/y
			print(x,y)	#float

			x=x^y
			y=x^y
			x=x^y
			print(x,y)
				
			x,y=y,x
			print(x,y)
				
#Sum of digits
			n=123
   		sum=0
			while n>0:
				d=n%10
				sum+=d
				n=n//10
			print(sum)

			num="1456"
			su=0
			for i in num:
				su+=int(i)
			print(su)
#Count vowels and consonants
			str1="vasu is a good a00 boy"
			str2="a"
			c=0
			for i in str1:
				if i==str2:
					c+=1
			print(c)
			print(str1.count("a"))
#Palindrome
			string = list(str)
			string.reverse()
			print("".join(string))
			if s==str:
				print('pali')
			else:
				print("not pali")
				
			s=""
			for i in str:
				s=i+s
			if s==str:
				print('pali')
			else:
				print("not pali")
'''