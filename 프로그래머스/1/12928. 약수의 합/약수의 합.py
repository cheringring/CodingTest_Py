def solution(n):
    answer = 0
    answer = sum(i for i in range(1, n + 1) if n % i == 0) #n을 12로 넣으면 실제적으로는 11까지 돌려짐.
    return answer