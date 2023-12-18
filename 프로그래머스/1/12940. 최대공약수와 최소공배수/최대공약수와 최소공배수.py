def solution(n, m):
    big = max(n, m)
    small = min(n, m)
    return [gcd(big, small), lcm(big, small)]
    
def gcd(big, small):
    r = 1
    while r:
        r = big % small
        big = small
        small = r
    
    return big
    
def lcm(big, small):
    div = gcd(big, small)
    return (big * small) // div