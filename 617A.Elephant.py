n = int(input())
count = 0
while(n):
    if n>=5:
        n -=5
        count += 1
    if n ==4 :
        n -= 4
        count += 1
    if n ==3 :
        n -= 3
        count += 1
    if n ==2 :
        n -= 2
        count += 1
    if n == 1:
        n -= 1
        count += 1
print(count)
