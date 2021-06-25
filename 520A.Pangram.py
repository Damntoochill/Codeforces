n = int(input())
s = input()
a = set()
for i in s:
    a.add(i.lower())
if len(a) ==26:
    print("YES")
else:
    print("NO")
