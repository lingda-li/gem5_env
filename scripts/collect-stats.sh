#!/bin/sh

if [ $# -ne 1 ]
then
    echo Usage: $0 stat_file
    exit
fi

cud=`pwd`
stat_file=$1
start_num=1
end_num=1

cur_num=$start_num
while [ $cur_num -le $end_num ]
do
    cur_stat=`head -n $cur_num $cud/scripts/statlist | tail -n 1`
    echo "********** $cur_stat **********"
    $cud/scripts/collect-single-stat.sh "$cur_stat" $stat_file
    echo

    cur_num=$(( cur_num+1 ))
done
