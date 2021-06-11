t = int(input())
s = [char for char in input()]
i = 0
count = 0
while(i<len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    i+=1
print(count)
