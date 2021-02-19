#User function Template for python3

class Solution:
    def distributeCandies(self, N, K):
        # code here
        arr = {}
        i = 1
        for j in range(1, K + 1):
            arr[j] = 0

        while True:

            if N <= i:
                arr[i] = arr[i]+N
                break
            else:
                arr[i % K] = arr[i % K] + i
                N = N - i
                i = i + 1
        return list(arr.values())

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        res = ob.distributeCandies(N,K)
        for i in res:
            print(i,end=" ")
# } Driver Code Ends
