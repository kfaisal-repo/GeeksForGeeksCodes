#User function Template for python3
import math
class Solution:
	def FindQuery(self, nums, Query):
		# Code here
		listl=[]
		p=pow(10,9)+7
		
		for i in Query:
		    j=i[0]
		    sum_l1=0
		    counter=1
		    
		    while j <= i[1]:
		        sum_l1=sum_l1 + math.fmod((math.fmod(math.pow(counter,2),p) * math.fmod(nums[j-1],p)),p)
		        j=j+1
		        counter=counter + 1
		    listl.append(int(sum_l1))
		return listl
		        
# math.fmod((pow(counter,2,p) * math.fmod(nums[j-1],p)),p)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		q = int(input())
		Query = []
		for i in range(q):
			Query.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.FindQuery(nums, Query)
		for _ in ans:
			print(_)


# } Driver Code Ends
