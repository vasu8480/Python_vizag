# #---------------------- only for level-1 flatten ----------------------
# l=[[7],[6,5],[1,2,3]]
# flat_list=[]
# for i in l:
# 	for val in i:
# 		flat_list.append(val)
# print(flat_list) # [7, 6, 5, 1, 2, 3]

# #Anagram
# s = "anagram"
# t = "nagaram"
# l = sorted(s)
# k = sorted(t)
# if l == k:
# 	print("True")
# else:
# 	print("False")

#Missing Number
# nums=[0,1,2,4]   # 0 has to be in the list
# currentSum = sum(nums)
# n = len(nums)
# intendedSum = n*(n+1)/2
# print(int(intendedSum-currentSum)) #output:3
