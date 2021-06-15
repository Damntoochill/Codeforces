n = int(input())
r = [int(i) for i in input().split()]
flag = 0
for i in r:
    if i == 1:
        flag = 1
if flag == 1:
    print('HARD')
else:
    print('EASY')
