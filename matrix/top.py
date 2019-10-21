import sys
def memorised(p):
    n=len(p)
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1,n):
        for j in range(i,n):
            m[i][j]=sys.maxsize
    return lookupchain(m,p,1,n-1)
def lookupchain(m,p,i,j):
    if m[i][j]<sys.maxsize:
        return m[i][j]
    if i==j:
        m[i][j]=0
    else:
        for k in range(i,j):
            q=lookupchain(m,p,i,k)+lookupchain(m,p,k+1,j)+p[i-1]*p[k]*p[j]
            if q<m[i][j]:
                m[i][j]=q
    return m[i][j]

arr = [1, 2, 3, 4, 3] 
n = len(arr); 
print("Minimum number of multiplications is ", 
				memorised(arr));
