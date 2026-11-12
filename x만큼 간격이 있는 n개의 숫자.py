def solution(x, n):
    answer = []
    z = x
    for i in range(n):
        answer.append(z)
        z += x
    return answer

print((solution(5, 15)))