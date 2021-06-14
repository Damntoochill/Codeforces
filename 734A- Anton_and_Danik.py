n = int(input())
s = list(input())
count_A = 0
count_B = 0
for i in s:
    if i == 'A':
        count_A += 1
    if i == 'D':
        count_B += 1
if count_B<count_A :
    print("Anton")
elif count_A<count_B:
    print("Danik")
else:
    print('Friendship')
