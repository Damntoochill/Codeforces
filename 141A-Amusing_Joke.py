dict1={}
flag = 0
for i in range(2):
    s = input()
    for j in s:
        if j not in dict1:
            dict1[j] = 1
        else:
            dict1[j] += 1
s = input()
for i in s:
    if i in dict1:
        dict1[i] -= 1
    else:
        flag = 1
        break
for i in dict1:
    if dict1[i] != 0:
        flag = 1
        break
    
if flag == 1:
    print("NO")
else:
    print("YES")
        
