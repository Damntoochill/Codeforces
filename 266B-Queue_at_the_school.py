n,k = map(int,input().split())
s = [x for x in input()]
for i in range(k):
    j = 1
    while(j<n):
        if s[j] == 'G' and s[j-1] == "B":
            s[j],s[j-1] = s[j-1],s[j]
            j += 2
        else:
            j+= 1
            
print("".join(x for x in s))
        
    
                
