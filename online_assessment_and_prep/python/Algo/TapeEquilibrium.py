# smallest absolute different bettween sum of the first part and the second part of the array
def solution(A):
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2*left_sum), m)
    return m

# right_sum = s - left_sum 
# difference = right_sum - left_sum 
# so difference = s - left_sum - left_sum or difference = s - 2 * left_sum
print(solution([3,1,2,4,3]))

