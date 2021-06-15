magnets= int(input())
poles = []
count = 1
for magnet in range(magnets):
    poles.append(input())
for i in range(magnets-1):
    if poles[i][1] == poles[i+1][0]:
        count += 1
        
print(count)
