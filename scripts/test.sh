#!/bin/sh

cud=`pwd`
gem5_dir="$cud/../gem5_sve"
gem5_bin="$gem5_dir/build/ARM/gem5.opt"
#gem5_bin="$gem5_dir/build/ARM/gem5.debug"
se_config_file="$gem5_dir/configs/example/se.py"
arch_cfg="--arm-sve-vl=8 --cpu-type O3_ARM_v7a_3 --caches --l2cache"
pim_cfg="--arm-sve-vl=8 --cpu-type O3_ARM_v7a_3 --caches --l2cache --enable-pim --pim-type=kernel --kernel-type=adder --num-pim-kernels=1 --mem-size=512MB --coherence-granularity=64B"
pim_fs_cfg="--enable-pim --pim-type=kernel --kernel-type=adder --num-pim-kernels=1 --coherence-granularity=64B"

#--debug-flags=PIM

#./build/X86/gem5.opt --debug-flags=PIM configs/example/se.py --cpu-type=TimingSimpleCPU --cpu-clock=2GHz --caches --l2cache --enable-pim --pim-type=kernel --kernel-type=adder --num-pim-kernels=1 --mem-size=512MB --coherence-granularity=64B -c ./tests/test-progs/pim-hello/hellopim
#/home/lli/git/spack/opt/spack/linux-ubuntu18.04-skylake/gcc-7.4.0/hpctoolkit-2019.08.14-wekyoh3ctdtob7tcs4updweh3mpdfv2h/bin/hpcrun $gem5_bin -d test/m5out $se_config_file $arch_cfg -c ../benchmarks_wombat/hello_gcc
$gem5_bin -d test/m5out $se_config_file $arch_cfg -c ../benchmarks_wombat/hello_gcc
#$gem5_bin -d test/m5out $se_config_file $arch_cfg -c ../benchmarks_wombat/sg.gcc8c.8sve.s
#$gem5_bin -d test/m5out --debug-flags=PIM $se_config_file $pim_cfg -c ../benchmarks_wombat/sg.gcc8c.8sve.s
#cp $gem5_bin bin/gem5.test
#/home/lli/git/spack/opt/spack/linux-ubuntu18.04-skylake/gcc-7.4.0/hpctoolkit-2019.08.14-wekyoh3ctdtob7tcs4updweh3mpdfv2h/bin/hpcrun $gem5_bin -d test/m5test /home/lli/simulation/env/../gem5_sve/configs/example/arm/fs_bigLITTLE.py --kernel vmlinux.4.15_64 --dtb armv8_gem5_v1_1cpu.dtb --disk aarch64-ubuntu-trusty-headless.img --restore-from /home/lli/simulation/env/res/vl64.at/mtc/cpt --arm-sve-vl=16 --cpu-type timing --caches --bootscript boot/mtc.vl64.rcS  --maxinsts 100000000 &
#time ./bin/gem5.test -d test/m5test /home/lli/simulation/env/../gem5_sve/configs/example/arm/fs_bigLITTLE.py --kernel vmlinux.4.15_64 --dtb armv8_gem5_v1_1cpu.dtb --disk aarch64-ubuntu-trusty-headless.img --restore-from /home/lli/simulation/env/res/vl64.at/mtc/cpt --arm-sve-vl=16 --cpu-type timing --caches --bootscript boot/mtc.vl64.rcS  --maxinsts 100000000 &
#./bin/gem5.test -d test/m5test --debug-flags=PIM /home/lli/simulation/env/../gem5_sve/configs/example/arm/fs_bigLITTLE.py --kernel vmlinux.4.15_64 --dtb armv8_gem5_v1_1cpu.dtb --disk aarch64-ubuntu-trusty-headless.img --restore-from /home/lli/simulation/env/res/vl64.at/mtc/cpt --arm-sve-vl=16 --cpu-type timing --caches --bootscript boot/mtc.vl64.rcS $pim_fs_cfg #--maxinsts 100000000 &
#./bin/gem5.test -d test/m5test --debug-flags=Exec,MemoryAccess,LSQUnit /home/lli/simulation/env/../gem5_sve/configs/example/arm/fs_bigLITTLE.py --kernel vmlinux.4.15_64 --dtb armv8_gem5_v1_1cpu.dtb --disk aarch64-ubuntu-trusty-headless.img --restore-from /home/lli/simulation/env/res/vl64.at/mtc/cpt --arm-sve-vl=16 --cpu-type timing --caches --bootscript boot/mtc.vl64.rcS  --maxinsts 10000000 &
