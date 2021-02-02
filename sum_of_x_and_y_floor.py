#User function Template for python3

import math
class Solution:
	def sumofproduct(self, n):
	    sum=0
	    for i in range(1,n+1):
	        j=math.floor(n/i)
	        if j <= n:
	            sum=sum+(i*j)
	    return sum
		# Code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.sumofproduct(n)
		print(ans)
# } Driver Code Ends
