dial = input()
sum = 0

for i in range(len(dial)):
    if dial[i] in "ABC":
        sum += 3
    if dial[i] in "DEF":
        sum += 4
    if dial[i] in "GHI":
        sum += 5
    if dial[i] in "JKL":
        sum += 6
    if dial[i] in "MNO":
        sum += 7
    if dial[i] in "PQRS":
        sum += 8
    if dial[i] in "TUV":
        sum += 9
    if dial[i] in "WXYZ":
        sum += 10
print(sum)