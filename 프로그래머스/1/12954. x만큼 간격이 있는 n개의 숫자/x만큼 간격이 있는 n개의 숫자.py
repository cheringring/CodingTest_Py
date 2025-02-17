def solution(x, n):
    #n은 인덱스 5개면 index 4개 까지
    #x부터 시작해서 x씩 증가.
    answer = []
    # x* i(i는 0부터 계속 증가), X간격만큼 증가니까
    # i 반복문 돌려서 n+1만큼 (range는 숫자 그 전까지 뽑아내니까)
    # 리스트 컴프리핸션을 써야될때는 대괄호 [] 를 이용해야함.
    answer = [x * i for i in range(1, n+1)]
    return answer