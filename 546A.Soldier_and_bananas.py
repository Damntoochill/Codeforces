k,n,w = map(int,input().split())
amt = 0
for i in range(1,w+1):
    amt = amt + i*k
if amt>=n:
    print(amt-n)
else:
    print(0)
