def solution(s):
    answer = ''
    le = len(s)
    sl = le // 2
    if le % 2 != 0:
        answer = s[sl]
    else:
        answer += s[sl-1]
        answer += s[sl]
    return answer

print(solution("helloworld"))