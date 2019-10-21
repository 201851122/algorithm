import sys 
def matrixmnaive(p, i, j): 
    if i == j: 
        return 0
    min = sys.maxsize 
    for k in range(i,j):
        count=(matrixmnaive(p,i,k)+matrixmnaive(p,k+1,j)+p[i-1]*p[k]*p[j])
        if count<min:
            min=count
    return min
   

arr =  [1, 2, 3, 4, 3]; 
n = len(arr); 
print("Minimum number of multiplications is ", 
				matrixmnaive(arr, 1, n-1)); 


