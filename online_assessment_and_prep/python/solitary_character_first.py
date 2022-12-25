def getSoliCharFirst(str):
    # write your code here
    # return the output
    str = str.lower()
    index=1
    for i in str:
        if str.count(i) == 1:
            #return i
            return index
        index+=1

def getSoliCharFirst_2(str):       
    for i in range(len(str)):
        if str.find(str[i]) == str.rfind(str[i]):
            return i+1
    return -1

print getSoliCharFirst('statistic')
print getSoliCharFirst_2('statistic')