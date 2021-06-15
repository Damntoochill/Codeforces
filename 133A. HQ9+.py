p = list(input())
a = ['H','Q','9']
flag = 0
for letter in p:
    if ord(letter) >= 33 and ord(letter) <= 126:
        if letter in a:
            flag = 1
            break
if flag == 1:
    print('YES')
else:
    print('NO')
