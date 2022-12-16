#assume input is a list of numbers [1, -15, 21]
#return the sum of the numbers, each number is less than 10^16, and need get absolute value of negative number

sum=0
limit=$(echo 10^16 | bc)

# read input 
# for num in $input
for num in `echo $*`
do
    # echo "$num"
    if [ ${num} -lt 0 ]
    then
        if [ `expr 0 - ${num}` -gt $limit ]
        then
            echo "exceed limit"
            exit 1
        fi
        sum=`expr ${sum} - ${num}`
    else
        if [ $num -gt $limit ]
        then
            echo "exceed limit"
            exit 1
        fi
        sum=`expr ${sum} + ${num}`
    fi
done
echo "${sum}"