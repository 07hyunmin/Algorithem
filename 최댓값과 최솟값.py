def solution(s):
    answer = ''
    s1 = list(map(int, s.split()))
    Max = max(s1)
    Min = min(s1)
    answer = f'{Min} {Max}'
    return answer

print(solution("38 34 15 14"))