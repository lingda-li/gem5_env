#!/bin/sh

cud=`pwd`
#gem5_dir="$cud/../gem5_sve"
gem5_dir="$cud/../gem5"
gem5_src_bin="$gem5_dir/build/ARM/gem5.opt"
if [ $# -ne 0 ]
then
    gem5_bin="$cud/bin/gem5.run$1"
else
    gem5_bin="$cud/bin/gem5.run"
fi
cp $gem5_src_bin $gem5_bin
