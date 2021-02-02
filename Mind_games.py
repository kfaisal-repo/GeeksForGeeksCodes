#User function Template for python3

from random import randint
class Solution:
    def mindGame(self, K):
        a=randint(1,10)
        return ((a*2 +K) >> 1) -a
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        K=int(input())
        
        ob = Solution()
        print(ob.mindGame(K))
# } Driver Code Ends
