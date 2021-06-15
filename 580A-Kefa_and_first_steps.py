t = int(input())
n = list(map(int,input().split()))
c = 1
cc = 1
for i in range(1,t):
    if n[i] >= n[i-1]:
        cc += 1
        if cc>c :
            c = cc
    else:
        cc =1
print(c)
