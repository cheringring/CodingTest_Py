import math

def solution(n):
    x = math.isqrt(n)
    # n의 제곱근
    if(x * x == n):
        return ( x + 1) ** 2
    else:
        return -1