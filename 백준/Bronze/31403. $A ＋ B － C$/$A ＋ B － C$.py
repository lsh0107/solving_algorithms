import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
s = ''

for _ in range(2):
    if isinstance(a, int) == True:
        print(a+b-c)
        a = str(a)
        b = str(b)
        
    else:
        s += a + b
        s = int(s)
        print(s-c)
        