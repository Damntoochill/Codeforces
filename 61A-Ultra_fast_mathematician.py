string1 = input()
string2 = input()
string3 = ""
for i in range(len(string1)):
    if string1[i] != string2[i]:
        string3 += '1'
    else:
        string3 += '0'

print(string3)
