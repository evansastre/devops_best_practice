
# write your code in Bash
rename_logname () {
    logtype=$1
    num_log=$(ls $logtype* | wc -l )
    #num_log=$(cat test-input-01.txt | jq . | grep $logtype | wc -l)
    echo $num_log

    if [ $num_log -eq 0 ]
    then
        echo notexist
        return
    fi
    if [ $num_log -eq 1 ] 
    then 
        echo $logtype $logtype.1
        mv $logtype $logtype.1
        touch $logtype
        return
    fi
    
    start=$num_log
    end=2
    for i in `seq $start $end`
    do  
        echo $logtype.$((i-1)) $logtype.$i
        mv $logtype.$((i-1)) $logtype.$i
    done    
    echo $logtype $logtype.1
    mv $logtype $logtype.1
    touch $logtype

}

rename_logname error.log
rename_logname access.log