def solution(A):
    check_A = set()
    for i in A:
        if i in check_A:
            return 0
        else:
            check_A.add(i)
    if max(check_A) == len(A):
        return 1

    return 0
