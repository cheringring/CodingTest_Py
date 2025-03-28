def solution(s):
    lencount = len(s)
    # / 는 float 형으로 반환, //는 int
    mid = lencount // 2 
    if lencount % 2 == 0:
        return s[mid - 1 : mid + 1]
    else:
        return s[mid]