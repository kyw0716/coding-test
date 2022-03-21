condition = list(map(int,input().split()))
cardNum = list(map(int,input().split()))

max = 0
sum = 0

for i in range(condition[0] - 2):
    sum += cardNum[i]
    for j in range(i + 1, condition[0] - 1):
        sum += cardNum[j]
        for k in range(j + 1,condition[0]):
            sum += cardNum[k]
            if sum > max and sum <= condition[1]:
                max = sum
            sum -= cardNum[k]
        sum -= cardNum[j]
    sum -= cardNum[i]

print(max)