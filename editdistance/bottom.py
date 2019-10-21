def editdistance(arr1, arr2, m, n): 
	dp = [[0 for x in range(n+1)] for x in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0: 
				dp[i][j] = j 
			elif j == 0: 
				dp[i][j] = i
			elif arr1[i-1] == arr2[j-1]: 
				dp[i][j] = dp[i-1][j-1] 
			else: 
				dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) 
	return dp[m][n] 

arr1 = "123456789"
arr2 = "987654321"
print("The distance is",editdistance(arr1, arr2, len(arr1), len(arr2))) 

