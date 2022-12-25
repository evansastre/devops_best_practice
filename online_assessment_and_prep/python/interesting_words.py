def getGrouped(words):
    # Write your code here
    groups=[]
    result=0
    for word in words:
        # Convert the word to a sorted list of characters
        chars = list(word)
        chars.sort()
        
        # Use the sorted list of characters as the key in the dictionary
        if chars in groups:
            pass
        else:
            result+=1
            groups.append(chars)
            
    return result

print getGrouped(['abc','acb','bac','bca','cab','dhc','efg'])
print getGrouped(['abc','dhc','efg','hdc','sfv'])