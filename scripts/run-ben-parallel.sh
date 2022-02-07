#!/bin/sh

if [ $# -ne 3 ]
then
    echo Usage: $0 testcase_name vector_length extra_arch_config
    exit
fi

case=$1
vl=$2

cud=`pwd`
gem5_dir="$cud/../gem5_sve"
gem5_bin="$cud/bin/gem5.run"
config_file="$gem5_dir/configs/example/arm/fs_bigLITTLE.py"
linux_cfg="--kernel vmlinux.4.15_64 --dtb armv8_gem5_v1_1cpu.dtb --disk aarch64-ubuntu-trusty-headless.img"
arch_cfg="--arm-sve-vl=16 --cpu-type timing --caches $3"
#arch_cfg="--arm-sve-vl=16 --cpu-type atomic"
res_path="$cud/res"
benchlist="$cud/scripts/benchlist_all"
#benchlist="$cud/scripts/benchlist_mtc"

if [ ! -f $gem5_bin ] || [ ! -f $config_file ]
then
    echo invalid file.
    exit
fi

# run benchmarks
ben_num=`wc -l $benchlist | awk '{print \$1}'`
cur_num=1
mkdir -p $res_path/$case
while [ $cur_num -le $ben_num ]
do
    ben=`head -n $cur_num $benchlist | tail -n 1`
    echo "********** $ben **********"
    $gem5_bin -d $res_path/$case/$ben $config_file $linux_cfg --restore-from $res_path/vl${vl}.at/$ben/cpt \
        $arch_cfg --bootscript boot/${ben}.vl${vl}.rcS &
    echo
    cur_num=$(( cur_num+1 ))
done

# complete
cd $cud
echo finish at `date`
