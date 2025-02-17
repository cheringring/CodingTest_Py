def solution(n):
    answer = 0

    #정수로 더해야하니까 int(x) 넣어주고
    #반복문할때 각 자릿씩 뽑기 위해 문자열로 변환시켜주고
    # for반복문을 통해 각 자릿수 하나씩 가져옴
    
    # n을 문자열로 변환 -> 한자릿씩 가져와서 x담음.
    # x를 정수화함. ->  sum
    answer = sum(int(x) for x in str(n))

    print('Hello Python')

    return answer
