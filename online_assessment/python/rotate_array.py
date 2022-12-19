def solution(A, K):
    # Implement your solution here
    arr_afterrotate=[]
    if len(A)==0:
        return A
    if K > len(A):
        K=K%len(A)
    if K==0:
        return A
    for i in range(len(A)-K, len(A)):
        arr_afterrotate.append(A[i])
    for i in range(0, len(A)-K):
        arr_afterrotate.append(A[i])
    
    return arr_afterrotate


print(solution([3, 8, 9, 7, 6], 3))

# A = [3, 8, 9, 7, 6]
# K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]