s = input()
currs = 0
sum = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        currs += 1
        if currs > sum:
            sum = currs
    else:
        currs = 0
if (sum+1)>=7:
    print("YES")
else:
    print("NO")
