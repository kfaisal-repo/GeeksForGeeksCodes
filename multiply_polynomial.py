# User function Template for python3
class Solution:
    def polyMultiply(self, Arr1, Arr2, M, N):
        # code here
        diction = {-1: -999}
        for i in range(1, M):
            for j in range(1, N):
                p = Arr1[i] * Arr2[j]
                if i + j not in diction.keys():
                    diction[i + j] = p
                else:
                    diction[i + j] = diction[i + j] + p
        return diction.values()


# {
#  Driver Code Starts
# Initial Template for Python 3

# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        M =4
        N=3

        Arr1 = input().split()

        Arr2 = input().split()

        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
