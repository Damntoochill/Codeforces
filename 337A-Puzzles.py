n, m = map(int,input().split())
f = list(map(int,input().split()))
f.sort()
diff = f[n-1] - f[0]
c_diff = 0
for i in range(len(f)-n+1):
    c_diff = f[i+n-1] - f[i]
    if c_diff<diff:
        diff = c_diff
        
print(diff)
