benchmark_list = [
  #('503.bwaves_r', '../run_base_test_mytest-64.0000/bwaves_r_base.mytest-64 bwaves_1 < bwaves_1.in'),
  ('507.cactuBSSN_r', '../run_base_test_mytest-64.0000/cactusBSSN_r_base.mytest-64 spec_test.par'),
  ('508.namd_r', '../run_base_test_mytest-64.0000/namd_r_base.mytest-64 --input apoa1.input --iterations 1 --output apoa1.test.output'),
  ('519.lbm_r', '../run_base_test_mytest-64.0000/lbm_r_base.mytest-64 20 reference.dat 0 1 100_100_130_cf_a.of'),
  ('521.wrf_r', '../run_base_test_mytest-64.0000/wrf_r_base.mytest-64'),
  ##('526.blender_r', '../run_base_test_mytest-64.0000/blender_r_base.mytest-64 cube.blend --render-output cube_ --threads 1 -b -F RAWTGA -s 1 -e 1 -a'),
  #('527.cam4_r', '../run_base_test_mytest-64.0000/cam4_r_base.mytest-64'),
  #('538.imagick_r', '../run_base_test_mytest-64.0000/imagick_r_base.mytest-64 -limit disk 0 test_input.tga -shear 25 -resize 640x480 -negate -alpha Off test_output.tga'),
  #('544.nab_r', '../run_base_test_mytest-64.0000/nab_r_base.mytest-64 hkrdenq 1930344093 1000'),
  #('549.fotonik3d_r', '../run_base_test_mytest-64.0000/fotonik3d_r_base.mytest-64'),
  ##('554.roms_r', '../run_base_test_mytest-64.0000/roms_r_base.mytest-64 < ocean_benchmark0.in.x'),
  #('997.specrand_fr', '../run_base_test_mytest-64.0000/specrand_fr_base.mytest-64 324342 24239'),
  ('500.perlbench_r', '../run_base_test_mytest-64.0000/perlbench_r_base.mytest-64 -I. -I./lib makerand.pl'),
  ('502.gcc_r', '../run_base_test_mytest-64.0000/cpugcc_r_base.mytest-64 t1.c -O3 -finline-limit=50000 -o t1.opts-O3_-finline-limit_50000.s'),
  ('505.mcf_r', '../run_base_test_mytest-64.0000/mcf_r_base.mytest-64 inp.in'),
  ('523.xalancbmk_r', '../run_base_test_mytest-64.0000/cpuxalan_r_base.mytest-64 -v test.xml xalanc.xsl')
  #('525.x264_r', '../run_base_test_mytest-64.0000/x264_r_base.mytest-64 --dumpyuv 50 --frames 156 -o BuckBunny_New.264 BuckBunny.yuv 1280x720'),
  #('531.deepsjeng_r', '../run_base_test_mytest-64.0000/deepsjeng_r_base.mytest-64 test.txt'),
  #('548.exchange2_r', '../run_base_test_mytest-64.0000/exchange2_r_base.mytest-64 0'),
  #('557.xz_r', '../run_base_test_mytest-64.0000/xz_r_base.mytest-64 cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1548636 1555348 0'),
  #('999.specrand_ir', '../run_base_test_mytest-64.0000/specrand_ir_base.mytest-64 324342 24239')
]

#benchmark_dir_prefix = '/../benchmarks_wombat/benchspec/CPU/'
benchmark_dir_prefix = '/../benchmarks_wombat/benchspec_1/CPU/'
benchmark_dir_postfix = '/run/run_base_test_mytest-64.0000'
