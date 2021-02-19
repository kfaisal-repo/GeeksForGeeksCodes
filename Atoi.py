# your task is to complete this function
# function should return an integer
def atoi(string):
    # Code here
    x=-1
    try:
        x=int(string)
    except ValueError as e:
        x=-1
    return x

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends
