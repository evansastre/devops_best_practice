def solution(X, Y, D):
    import math
    last_jump=(Y-X)%D
    if last_jump==0:
        return math.trunc((Y-X)/D)
    else:
        return math.trunc((Y-X)/D) + 1

print(solution(10, 85, 30))
print(solution(1, 5, 2))
print(solution(5, 1000000000, 2))

