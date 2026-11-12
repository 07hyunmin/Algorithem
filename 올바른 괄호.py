def solution(s):
    answer = True
    count = 0
    
    for i in range(len(s)):
        if s[0] == ')':
            return False
        if s[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    if count > 0:
        return False
        
        
    print('Hello Python')

    return True

print(solution("(()))))((()))"))