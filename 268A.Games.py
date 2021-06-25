n = int(input())
teams = []
count = 0
for i in range(n):
    teams.append(list(map(int,input().split())))
for i in range(n-1):
    for j in range(i,n):
        if teams[i][0] == teams[j][1]:
            count += 1
        if teams[i][1] == teams[j][0]:
            count += 1
print(count)
