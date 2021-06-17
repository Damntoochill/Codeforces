n = int(input())
p = list(map(int,input().split()))
total = n*100
total_orange = 0
for i in p:
    total_orange += i

print(total_orange*100/total)
