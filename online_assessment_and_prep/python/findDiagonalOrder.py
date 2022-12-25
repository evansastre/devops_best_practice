class Solution:
    def findDiagonalOrder(self, mat): # -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        # find the number of diagonals in the matrix (m + n - 1)
        for i in range( m + n - 1):
            # if the diagonal is odd, we start from the bottom and go up (i start from 0)
            if i % 2 == 0:
                for j in range(i, -1, -1):
                    if j < m and i - j < n:
                        result.append(mat[j][i - j])
            # if the diagonal is even, we start from the top and go down
            else:
                for j in range(i + 1):
                    if j < m and i - j < n:
                        result.append(mat[j][i - j])
                
        return result
print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))



class Solution2:
    def findDiagonalOrder(self, mat): # -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        for k in range(m+n-1):
            if k < n:
                i = 0
                j = k 
                intermediate = []
                while j>=0 and i<m:
                    intermediate.append(mat[i][j])
                    # print(intermediate)
                    i+=1
                    j-=1
                if k%2 ==0:
                    result.extend(intermediate[::-1])
                else:
                    result.extend(intermediate)
            elif k>=n:
                i = k -n +1
                j = n -1 
                intermediate = []
                while j>=0 and i<m:
                    intermediate.append(mat[i][j])
                    i+=1
                    j-=1
                if k%2 ==0:
                    result.extend(intermediate[::-1])
                else:
                    result.extend(intermediate)
        return result

print(Solution2().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution2().findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# mat[2][2] =11 
# mat[1][3]=8
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12

# m = 3 
# n = 4 

# i = 4 - 4 +
# j = 3, 2, 1, 0


# mat[3][3-3]=  (j<m)
# mat[2][3-2] = 10
# mat[1][3-1] = 7
# mat[0][3-0] = 4

# 4 7 10


#########################################################
# 1 2 3 
# 4 5 6
# 7 8 9

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -10^5 <= mat[i][j] <= 10^5


# m: number of lines
# n: number of columns