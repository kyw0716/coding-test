N = input();
number = []

def find(Num):
    for i in range(int(Num)):
        array(i)
        c = i
        for n in number:
            c += int(n)
        if int(c) == int(Num):
            return i
        number.clear()
    return 0

def array(Num):
    for n in str(Num):
        number.append(n)
        
print(find(int(N)))