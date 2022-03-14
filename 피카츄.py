import re

pikachu = input()

pikachu = re.sub("pi|ka|chu","",pikachu)

if len(pikachu) == 0:
    print("YES")
else:
    print("NO")