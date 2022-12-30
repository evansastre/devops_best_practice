def solution(X, A):
    positions = set()
    for i in range(len(A)):
        if A[i] <= X and A[i] not in positions:
            positions.add(A[i])
        if len(positions) == X:
            return i
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(5, [3]))
print(solution(5, [2,2,2,2,2]))