def Rod_cut(p,n):
    size = 2**(n-1)
    string = [0]*size
    sub_str_len = n-1
    for i in range(size):
        s = ''
        a,count = i,0 
        while(a>0):
            s = str(a%2)+s
            a = a//2 
            count+=1 
        for j in range(count,sub_str_len):
            s = '0'+s 
        string[i] = s 
    maxi = 0 
    for i in range(size):
        price = 0
        pri = 0 
        count = 0 
        s = string[i] 
        k = 1 
        for j in range(len(s)-1,-1,-1):
            if s[j]=='1':
                price = price+p[k-pri]
                pri = k 
            k+=1 
        price = price+p[k-pri]
        maxi = max(maxi,price) 
    return maxi 
p = [0,1, 5, 8, 9, 10, 17, 17, 20] 
n = int(input("Enter the length of rod:- ")) 
ans = Rod_cut(p,n)
ans = max(ans,p[0]*n) 
print("Max Revenue for given length of rod is "+str(ans))