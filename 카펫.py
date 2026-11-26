def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for h in range(3, sum + 1):
        if sum % h == 0:
            w = sum // h
            if w >= h and (w - 2) * (h - 2) == yellow:
                return [w, h]
    return answer

print(solution(10, 2))