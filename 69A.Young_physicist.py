t = int(input())
x = []
y = []
z = []
for i in range(t):
    s = input().split()
    x.append(int(s[0]))
    y.append(int(s[1]))
    z.append(int(s[2]))
sum = 0
for i in x:
    sum += i
if sum == 0:
    for i in y:
        sum += i
    if sum == 0:
        for i in z:
            sum += i
        if sum == 0:
            print("YES")
else:
    print("NO")
