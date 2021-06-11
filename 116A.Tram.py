t  = int(input())
current = 0
max = 0
for i in range(t):
    a,b = map(int,input().split())
    current += b-a
    if current>max:
        max = current
print(max)
