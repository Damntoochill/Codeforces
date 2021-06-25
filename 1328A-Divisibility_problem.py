n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a<=b:
        print(b-a)
    else:
        c = a%b
        if c == 0:
            print(c)
        else:
            print(b-c)
