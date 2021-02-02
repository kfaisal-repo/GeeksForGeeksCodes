#User function Template for python3

import math

class Solution:
    def getHypotenuse(self, N):
        # code here 
        a=math.sqrt(2*N)
        return math.floor(math.sqrt(2*a*a))



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getHypotenuse(N))
# } Driver Code Ends
