s = input()
u_count = 0
l_count = 0
for i in s:
    if i.isupper():
        u_count += 1
    else:
        l_count+=1
if u_count > l_count:
    print(s.upper())
else:
    print(s.lower())
