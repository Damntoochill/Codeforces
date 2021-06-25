g = input()
if g == '{}':
    print(0)
else:
    x = set(g[1:len(g)-1].split(", "))
    print(len(x))
