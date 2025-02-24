def solution(absolutes, signs):
    i = 0
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = absolutes[i] * -1
        else:
            absolutes[i] = absolutes[i]
    return sum(absolutes)
            
            