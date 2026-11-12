def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer

print(solution([3,5,2,5,7,8,9,91,14,2], 4))