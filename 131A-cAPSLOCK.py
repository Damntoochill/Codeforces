string = input()
string2 = ''
if string == string.upper():
    for i in range(len(string)):
        string2 += string[i].lower()
elif string[0] != string[0].upper and string[1:] == string[1:].upper():
     for i in range(len(string)):
        if i == 0:
            string2 += string[i].upper()
        else:
            string2 += string[i].lower()
else:
    string2 = string
print(string2)
