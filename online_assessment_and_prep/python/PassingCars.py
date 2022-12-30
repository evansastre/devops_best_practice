def solution(A):
    # write your code in Python 3.6
    zeros = 0
    passing = 0
    for i in A:
        if i == 0:
            zeros += 1
        else:
            passing += zeros
    return passing

# 0 east
# 1 west

print(solution([0, 1, 0, 1, 1]))