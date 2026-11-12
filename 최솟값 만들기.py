def solution(A,B):
    answer = 0
    sum = 0
    
    sA = sorted(A)
    lB = sorted(B, reverse = True)
    for i in range(len(A)):
        sum += sA[i] * lB[i]

    return sum

print(solution([1, 4, 2], [5, 4, 4]))