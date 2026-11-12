def solution(n):
    answer = ''
    even = 0
    for i in range(n):
        if even % 2 == 0:
            answer += "수"
            even += 1
        else:
            answer += "박"
            even += 1
    return answer

print(solution(8))