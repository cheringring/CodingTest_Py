def solution(seoul):
    answer = ''
    x = 0
    for x in range(len(seoul)):
        if (seoul[x] == "Kim"):
            return f"김서방은 {x}에 있다"
    ## 다른 방법 
    ##  def solution(seoul):
    #   return f"김서방은 {seoul.index('Kim')}에 있다"