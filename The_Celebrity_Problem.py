#User function Template for python3

class Solution:
    def celebrity(self, M, n):
        inde=-1
        counter=1
        
        # code here 
        for i in range(0,n):
            counter=0
            for j in range(0,n):
                if M[j][i] == 1 or (j == i and M[j][i] == 0):
                    counter = counter + 1
            if counter == n:
                inde=i
                break
        return inde
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends
