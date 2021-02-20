# User function Template for python3
import copy
class Solution:
    def firstElement(self, n):
        original_matr=[[1,1],[1,0]]
        output_mat=[[1,1],[1,0]]
        empty_mat=[[1,1],[1,0]]
        p=1000000007

        for i in range(1,n):

            t = (original_matr[0][0] * output_mat[0][0]) + (original_matr[0][1] * output_mat[1][0])
            if t >= p:
                empty_mat[0][0]=t %p
            else:
                empty_mat[0][0]= t
            ##############################
            t = (original_matr[0][0] * output_mat[0][1]) + (original_matr[0][1] * output_mat[1][1])
            if t >= p:
                empty_mat[0][1]=t %p
            else:
                empty_mat[0][1]= t

            ##############################
            t = (original_matr[1][0] * output_mat[0][0]) + (original_matr[1][1] * output_mat[1][0])
            if t >= p:
                empty_mat[1][0] = t % p
            else:
                empty_mat[1][0] = t
            ##############################
            t = (original_matr[1][0] * output_mat[0][1]) + (original_matr[1][1] * output_mat[1][1])
            if t >= p:
                empty_mat[1][1] = t % p
            else:
                empty_mat[1][1] = t
            ##############################

            output_mat=copy.deepcopy(empty_mat)


        return empty_mat[1][0]

# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends
