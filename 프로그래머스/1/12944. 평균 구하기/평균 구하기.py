def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr) 
    return answer

# 다른방법 : numpy.mean()사용
# import numpy as np
# numpy.mean(arr)