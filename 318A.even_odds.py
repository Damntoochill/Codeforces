n,k = map(int, input().split())
even = 0
if n % 2 == 0:
    even = 1
if even:
    mid = int(n/2)
    if k > mid:
        i = 2*(k-mid)
    else:
        i = 1 + 2*(k-1)
else:
    mid = int((n+1)/2)
    if k > mid:
        i = 2*(k-mid)
    else:
        i = 1 + 2*(k-1)
print(i)
        
          
