n, h = map(int,input().split())
s = [int(x) for x in input().split()]
width = 0
for i in s:
    if i>h:
        width += 2
    else:
        width +=1
print(width)
