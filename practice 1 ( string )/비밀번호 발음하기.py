from asyncio import gather

testCaseArray = []
output = []

#모음이 있는지 판별
def aeiou(testCase):
    gather = "aeiou"
    find = 0
    for g in gather:
        if testCase.find(g) == -1:
            find += 1
    if find == 5:
        return "not acceptable"
    else :
        return "acceptable"

#연속되는 두개의 문자 판별
def two(testCase):
    for i in range(len(testCase)):
        if i == len(testCase) - 1:
            return "acceptable"
        if testCase[i] == testCase[i + 1] and testCase[i] != 'o' and testCase[i] != 'e':
            return "not acceptable"

#연속되는 3개의 모음, 자음 판별
def three(testCase):
    g = "aeiou"
    c = "qwrtypsdfghjklzxcvbnm"
    classify = ""
    for t in testCase:
        if t in c:
            classify += "c"
        else:
            classify += "g"
    if "ccc" in classify:
        return "not acceptable"
    if "ggg" in classify:
        return "not acceptable"
    return "acceptable"
        

#입력 부분
while True:
    testCase = input()
    if testCase == "end":
        break
    testCaseArray.append(testCase)

for testCase in testCaseArray:
    if aeiou(testCase) == "acceptable" and two(testCase) == "acceptable" and three(testCase) == "acceptable":
        output.append(f"<{testCase}> is acceptable.")
    else:
        output.append(f"<{testCase}> is not acceptable.")

for o in output:
    print(o)