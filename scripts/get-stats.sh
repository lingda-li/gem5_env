#!/bin/sh

if [ $# -ne 1 ]
then
    echo Usage: $0 testcase_name
    exit
fi

#postfix="_rs"
#postfix="_pb"
#postfix="_all"
#postfix="_spec"
#postfix="_spectest_test"
postfix="_spectest_train"
#postfix="_npb_s"
#postfix="_mm"

cud=`pwd`
input_path="$cud/res/$1"
output_file="$cud/stats/${1}${postfix}"
rm -f $output_file
stats_num=`wc -l $cud/scripts/statlist | awk '{print \$1}'`
benchlist="$cud/scripts/benchlist$postfix"

ben_num=`wc -l $benchlist | awk '{print \$1}'`
cur_num=1
while [ $cur_num -le $ben_num ]
do
    ben=`head -n $cur_num $benchlist | tail -n 1`
    benlog=$input_path/$ben/stats.txt
    if [ ! -f $benlog ]; then
        echo $benlog not found.
        cur_num=$(( cur_num+1 ))
        continue
    fi

    #echo "********** $ben **********" >> $output_file
    stat_num=1
    while [ $stat_num -le $stats_num ]
    do
        cur_stat=`head -n $stat_num $cud/scripts/statlist | tail -n 1`
        if [ ! "$cur_stat" ]; then
            break
        fi
        if [[ "$cur_stat" == "#"* ]]; then
            continue
        fi
        grep "$cur_stat" $benlog | tail -n 1 >> $output_file
        output=`grep "$cur_stat" $benlog | tail -n 1`
        if [ -z "$output" ]; then
            echo "$cur_stat    0" >> $output_file
        fi
        stat_num=$(( stat_num+1 ))
    done
    #echo                              >> $output_file

    cur_num=$(( cur_num+1 ))
done
