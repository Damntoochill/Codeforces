s = list(map(int,input().split('+')))
s.sort()
s1 = ""
s1 = "+".join(str(i) for i in s)
print(s1)
