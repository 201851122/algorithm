 
def editdistance(arr1, arr2, m , n):  
	if m==0: 
		return n 
		return m 
	if arr1[m-1]==arr2[n-1]: 
		return editdistance(arr1,arr2,m-1,n-1) 
	return 1 + min(editdistance(arr1, arr2, m, n-1),  
				editdistance(arr1, arr2, m-1, n), 
				editdistance(arr1, arr2, m-1, n-1)
				) 

arr1 = "123456789"
arr2 = "987654321"
print("The distance is",editdistance(arr1, arr2, len(arr1), len(arr2))) 


