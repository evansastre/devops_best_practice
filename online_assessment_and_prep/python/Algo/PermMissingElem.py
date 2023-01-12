def solution(A):
    if len(A)==0:
        return 1
    A_SET=set()
    for i in A: 
        if i in A_SET:
            return -1
        else: 
            A_SET.add(i)
    
    for i in range(1,len(A)+2):
        if i not in A_SET:       
            return i


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([5, 3, 6, 4, 7, 2]))