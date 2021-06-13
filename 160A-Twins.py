n = int(input())
coins = list(map(int,input().split()))
total = 0
count = 0
sum = 0
for i in coins:
    total += i
coins.sort(reverse = True)
for i in coins:
    sum += i
    count += 1
    if sum>total/2:
        break
print(count)
    
