#def solution(numbers):
#   result = 0
#    for i in range(10):
#        if i not in numbers:
#            result = result + i
#    return result
def solution(numbers):
    result = set(range(10)) - set(numbers)
    result2 = sum(result)
    return result2