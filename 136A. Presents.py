n = int(input())
f = list(map(int,input().split()))
a = [0 for i in range(n)]
for i,j in enumerate(f):
    a[j-1] = i+1
for i in a:
    print(i,end = " ")
    
