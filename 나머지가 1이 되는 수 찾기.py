def solution(n):
    answer = 0
    x = 1
    while True:
        a = n % x
        if a == 1:
            answer = x
            break
        x += 1
    return answer

print(solution(56))