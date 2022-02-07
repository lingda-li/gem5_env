#!/bin/sh

if [ $# -ne 1 ]
then
    echo Usage: $0 number_of_testcases
    exit
fi

postfix="_all"

test_num=`ls -tr res | wc -l`
cur_num=1

if [ $# -eq 1 ] && [ $1 -le $test_num ]; then
    cur_num=$((test_num-$1+1))
    echo "Generate for the latest $1 cases."
elif [ $# -eq 1 ]; then
    echo "Generate for all cases."
fi

while [ $cur_num -le $test_num ]
do
    testname=`ls -tr res | head -n $cur_num | tail -n 1`
    resfile="stats/$testname$postfix"

    if [ -f $resfile ] && [ $# -eq 0 ]; then
#echo ignore $testname.
        :
    elif [ `echo $testname | grep original` ] && [ $# -eq 0 ]; then
#echo ignore $testname.
        :
    else
        echo generate result for $testname
        ./scripts/get-stats.sh $testname
    fi

    cur_num=$(( cur_num+1 ))
done
