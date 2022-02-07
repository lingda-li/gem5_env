#!/bin/sh

if [ $# -ne 2 ]
then
    echo Usage: $0 stat_name stats_file
    exit
fi

grep $1 $2 | awk '{print $2}'
