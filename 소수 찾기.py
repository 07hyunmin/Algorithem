def solution(n):
    answer = 1
    s = [2]
    for i in range(3, n + 1):
        sw = False
        for j in s:
            if j * j > i:
                break
            if i % j == 0:
                sw = True
                break
        if not sw:
            s.append(i)
            answer+=1
    return answer

print(solution(32))