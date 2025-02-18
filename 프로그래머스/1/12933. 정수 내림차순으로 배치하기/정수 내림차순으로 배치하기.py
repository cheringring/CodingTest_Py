def solution(n):
    answer = 0
    # sorted 쓰면 리스트로 변환되어서 
    # join은 리스트의 요소들을 하나의 문자열로합침.
    answer = int("".join(sorted(str(n))[::-1]))
    # [::-1] 대신 reversed = True 써도됨.
    return answer