def smallest(x, y, z):
    if (x < y) and (x < z):
        small = x
    elif (y < x) and (y < z):
        small = y
    else:
        small = z
    return small
def editdistance(arr1,arr2,m,n,dp):
    if m==0:
        return n 
    if n==0:
        return m
    if dp[m-1][n-1] != -1 :
        return dp[m-1][n-1]
    if arr1[m-1] == arr2[n-1]:
         dp[m-1][n-1]=editdistance(arr1,arr2,m-1,n-1,dp)
         
    dp[m-1][n-1]=1+min(editdistance(arr1,arr2,m-1,n-1,dp),editdistance(arr1,arr2,m,n-1,dp),editdistance(arr1,arr2,m-1,n,dp)) 
    return dp[m-1][n-1]

arr1="123456789"
arr2="987654321"
maximum=10000
m=len(arr1)
n=len(arr2)
dp = [[-1 for x in range(maximum)] for x in range(m)]
print("The distance is",editdistance(arr1,arr2,m,n,dp))