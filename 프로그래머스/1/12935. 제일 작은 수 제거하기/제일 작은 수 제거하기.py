def solution(arr):
    if len(arr) <= 1:
        return [-1]
    # 리스트에서 특정 값을 지울려면 리스트.remove 통해 지워야됨.
    arr.remove(min(arr))
    return arr