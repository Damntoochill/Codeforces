n = int(input())
s = list(map(int,input().split()))
short = s[0]
tall = s[0]
s_index,t_index = 0,0
for i in range(n):
    if s[i]<=short:
        short = s[i]
        s_index = i
    if s[i]>tall:
        tall = s[i]
        t_index = i
s_steps = n-s_index-1
t_steps = t_index
if s_steps+t_steps>=n:
    print(s_steps + t_steps - 1)
else:
    print(s_steps + t_steps)
    
