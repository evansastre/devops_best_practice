def findlongestbinarygap(n):
    binary = bin(n)
    print(binary)
    binary = binary[2:]
    print(binary)
    longest_gap = 0
    gap = 0
    gaps = []
    for i in binary:
        if i == '0':
            gap += 1
        else:
            gaps.append(gap)
            gap = 0
    
    print(gaps)
    for gap in gaps:
        if gap > longest_gap:
            longest_gap = gap
    return longest_gap

print(findlongestbinarygap(1041))
print(findlongestbinarygap(32))

# 9 
# 1001
# 8
# 1000
# 33
# 100001 

# [0,2]

# [0]

#  10000010001
#  [0,5,3]