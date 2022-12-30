def solution(A):
    result = set()
    for i in A:
        if i > 0:
            result.add(i)

    if len(result) == 0:
        return 1

    for i in range(1, max(result) + 1):
        if i not in result:
            return i
    return max(result) + 1

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 3, 5, 4, 1, 2]))