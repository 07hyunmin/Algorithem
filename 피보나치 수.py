def solution(n):
    answer = 0
    fi = [0, 1]
    for i in range(2, n + 1):
        fi.append(fi[i - 1] + fi[i - 2])
    answer = fi[n] % 1234567
    return answer

print(solution(6))