def solution(s):
    answer = ''
    even = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            even = 0
            continue
        if even % 2 == 0:
            answer += s[i].upper()
            even += 1
        else:
            answer += s[i].lower()
            even += 1
    return answer

print(solution("hello world"))