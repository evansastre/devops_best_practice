def multiple_three_five(number):
    if number%3==0:
        max_3_multiple=int(number/3)-1
    else:
        max_3_multiple=int(number/3)
    #333
    print(max_3_multiple)
    if number%5==0:
        max_5_multiple=int(number/5)-1
    else:
        max_5_multiple=int(number/5)
    print(max_5_multiple)

    if number%15==0:
        max_15_multiple=int(number/15)-1
    else:
        max_15_multiple=int(number/15)
    print(max_15_multiple)
    # 200
    #total_3_multiple=(1+2+3…+333)*3
    sum=0
    for i in range(max_3_multiple+1):
	    sum+=i
    # sum = n(n+1)/2 = max_3_multiple(max_3_multiple+1)/2
    total_3_multiple = sum*3
    print(total_3_multiple)

    #total_3_multiple=(1+2+3+...200)*5
    sum=0
    for i in range(max_5_multiple+1):
	    sum+=i
    total_5_multiple = sum*5
    print(total_5_multiple)

    sum=0
    for i in range(max_15_multiple+1):
	    sum+=i
    total_15_multiple = sum*15
    print(total_15_multiple)
    
    total = total_3_multiple + total_5_multiple - total_15_multiple
    return total

print(multiple_three_five(1000))



# ∑k1=13333k1+∑k2=11995k2−∑k3=16615k3=166833+99500−33165=233168,
# where we have the used the identity
# ∑k=1nk=12n(n+1).