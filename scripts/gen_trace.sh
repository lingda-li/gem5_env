#!/bin/sh

vl=64
cud=`pwd`
#gem5_dir="$cud/../gem5_sve"
gem5_dir="$cud/../gem5"
gem5_bin="$gem5_dir/build/ARM/gem5.opt"
cp $gem5_bin bin/gem5.test
config_file="$gem5_dir/configs/example/arm/fs_bigLITTLE.py"
linux_cfg="--kernel vmlinux.4.15_64 --dtb armv8_gem5_v1_1cpu.dtb --disk aarch64-ubuntu-trusty-headless.img"
#arch_cfg="--arm-sve-vl=16 --cpu-type timing --caches --maxinsts 1000000000"
#arch_cfg="--arm-sve-vl=16 --cpu-type atomic"
arch_cfg="--cpu-type timing --caches --maxinsts 1000000000"
res_path="$cud/res"
#benchlist="$cud/scripts/benchlist_trace_p38"
benchlist="$cud/scripts/benchlist_trace"

if [ ! -f $gem5_bin ] || [ ! -f $config_file ]
then
    echo invalid file.
    exit
fi

# run benchmarks
ben_num=`wc -l $benchlist | awk '{print \$1}'`
cur_num=1
while [ $cur_num -le $ben_num ]
do
    ben=`head -n $cur_num $benchlist | tail -n 1`
    echo "********** $ben **********"
    #./bin/gem5.test -d test/m5test $config_file $linux_cfg --restore-from $res_path/vl${vl}.at/$ben/cpt \
    #    $arch_cfg --bootscript boot/${ben}.vl${vl}.rcS
    ./bin/gem5.test -d test/m5test $config_file $linux_cfg --restore-from $res_path/at/$ben/cpt \
        $arch_cfg --bootscript boot/${ben}.vl${vl}.rcS \
        --bootloader $gem5_dir/system/arm/bootloader/arm64/boot.arm64
    scp trace.txt hpc1:/lfs1/work/lli/trace_spec_q/${ben}.txt
    scp sq.trace.txt hpc1:/lfs1/work/lli/trace_spec_q/${ben}.sq.txt
    rm trace.txt sq.trace.txt
    echo
    cur_num=$(( cur_num+1 ))
done

# complete
cd $cud
echo finish at `date`
