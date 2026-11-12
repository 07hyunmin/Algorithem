def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    ave = answer / len(arr)
    return ave

print(solution([2,5,23,12,7,8,100]))