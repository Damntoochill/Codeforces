n = int(input())
count = 0
while(n):
    p, q = map(int,input().split())
    if q-p >= 2:
        count += 1
    n -= 1
print(count)
