def solution(x):
    i_sum = 0
    b = int(x)
## 각 자릿수에 접근하려면 문자열로 변환해야한다.
    a = str(x)
    for i in a:
        i_sum = i_sum + int(i)
    if b % i_sum == 0:
        return True
    else:
        return False