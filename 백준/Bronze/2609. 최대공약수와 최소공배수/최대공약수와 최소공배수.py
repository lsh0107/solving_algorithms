import sys

input = sys.stdin.readline
a, b = map(int, input().split())

def gcd(a, b):
    r = 1
    if a > b:
        while r:
            r = a%b
            a = b
            b = r   
        return a
    
    while r:
        r = b%a
        b = a
        a = r
    return b

def lcm(a, b):
    div = gcd(a, b)
    return (a * b) // div  

print(gcd(a, b))
print(lcm(a, b))