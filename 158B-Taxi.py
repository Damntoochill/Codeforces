n = int(input())
g = list(map(int,input().split()))
count = 0
dict = {1:0,2:0,3:0,4:0}
for i in g:
    dict[i] += 1
if dict[4] > 0:
    count += dict[4]
if dict[3]>0 and dict[1] > 0:
    if dict[3] >= dict[1]:
        count += dict[1]
        dict[3] -= dict[1]
        dict[1] = 0
    else:
        count += dict[3]
        dict[1] -= dict[3]
        dict[3] = 0
if dict[3]>0:
    count += dict[3]
if dict[2] > 0 and dict[1] > 0:
    if dict[2] %2 == 0:
        count += int(dict[2]/2)
        dict[2] = 0
    else:
        count += int(dict[2]//2) + 1
        dict[1] -= 2
        dict[2] = 0
if dict[2] > 0:
    if dict[2] %2 == 0:
        count += int(dict[2]/2)
    else:
        count += int(dict[2]//2) + 1
if dict[1] >0 :
    count += int((dict[1] + 3)/4)
    
print(count)

