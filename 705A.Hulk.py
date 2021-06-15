n = int(input())
mood = ['love', 'hate']
if n % 2 == 0:
    for i in range(n,0,-1):
        if i == 1:
            print('I love it')
            break
        if i%2 == 0:
            mood = 'hate'
            print('I ' + mood + ' that', end = " ")
        else:
            mood = 'love'
            print('I ' + mood + ' that', end = " ")
else:
    for i in range(n,0,-1):
        if i == 1:
            print('I hate it')
            break
        if i%2 == 0:
            mood = 'love'
            print('I ' + mood + ' that', end = " ")
        else:
            mood = 'hate'
            print('I ' + mood + ' that', end = " ")
