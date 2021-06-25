n = int(input())
a = list(map(int,input().split()))
count_even = []
count_odd = []
for i in a:
    if i%2 ==0:
        count_even.append(i)
    else:
        count_odd.append(i)
    if len(count_odd) >= 1 and len(count_even) >= 1:
        if len(count_even) > len(count_odd):
            print(a.index(count_odd[0])+1)
            break
        if len(count_even) < len(count_odd):
            print(a.index(count_even[0])+1)
            break
