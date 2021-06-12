s = input()
s1 = "hello"
j = 0
count = 0
for i in s:
    if i == s1[j]:
        j += 1
        count += 1
    if count == 5:
        break
if count ==5:
    print("YES")
else:
    print("NO")
