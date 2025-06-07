import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


#l=[input() for _ in range((int(input())))]
n=int(input())
l=[]
for i in range(n):
    row=input()
    l.append(row)

for i in l:
    m = list(map(lambda x: x.upper() if i.index(x) % 2 == 0 else x.lower(), i))
    print("".join(m))
