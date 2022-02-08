benchmark_list = [
  #('503.bwaves_r', '../run_base_refrate_mytest-64.0000/bwaves_r_base.mytest-64 bwaves_1 < bwaves_1.in'),
  ('507.cactuBSSN_r', '../run_base_refrate_mytest-64.0000/cactusBSSN_r_base.mytest-64 spec_ref.par', 85),
  ('508.namd_r', '../run_base_refrate_mytest-64.0000/namd_r_base.mytest-64 --input apoa1.input --output apoa1.ref.output --iterations 65', 36),
  ('510.parest_r', '../run_base_refrate_mytest-64.0000/parest_r_base.mytest-64 ref.prm', 96),
  ('511.povray_r', '../run_base_refrate_mytest-64.0000/povray_r_base.mytest-64 SPEC-benchmark-ref.ini', 28),
  ('519.lbm_r', '../run_base_refrate_mytest-64.0000/lbm_r_base.mytest-64 3000 reference.dat 0 0 100_100_130_ldc.of', 52),
  ('521.wrf_r', '../run_base_refrate_mytest-64.0000/wrf_r_base.mytest-64', 33),
  #('526.blender_r', '../run_base_refrate_mytest-64.0000/blender_r_base.mytest-64 sh3_no_char.blend --render-output sh3_no_char_ --threads 1 -b -F RAWTGA -s 849 -e 849 -a'),
  ('527.cam4_r', '../run_base_refrate_mytest-64.0000/cam4_r_base.mytest-64', 52),
  ('538.imagick_r', '../run_base_refrate_mytest-64.0000/imagick_r_base.mytest-64 -limit disk 0 refrate_input.tga -edge 41 -resample 181% -emboss 31 -colorspace YUV -mean-shift 19x19+15% -resize 30% refrate_output.tga', 77),
  ('544.nab_r', '../run_base_refrate_mytest-64.0000/nab_r_base.mytest-64 1am0 1122214447 122', 76),
  ('549.fotonik3d_r', '../run_base_refrate_mytest-64.0000/fotonik3d_r_base.mytest-64', 81),
  #('554.roms_r', '../run_base_refrate_mytest-64.0000/roms_r_base.mytest-64 < ocean_benchmark2.in.x', 81),
  ('997.specrand_fr', '../run_base_refrate_mytest-64.0000/specrand_fr_base.mytest-64 1255432124 234923', 1),
  ('500.perlbench_r', '../run_base_refrate_mytest-64.0000/perlbench_r_base.mytest-64 -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1', 16),
  ('502.gcc_r', '../run_base_refrate_mytest-64.0000/cpugcc_r_base.mytest-64 gcc-pp.c -O3 -finline-limit=0 -fif-conversion -fif-conversion2 -o gcc-pp.opts-O3_-finline-limit_0_-fif-conversion_-fif-conversion2.s', 80),
  ('505.mcf_r', '../run_base_refrate_mytest-64.0000/mcf_r_base.mytest-64 inp.in', 27),
  #('520.omnetpp_r', '../run_base_refrate_mytest-64.0000/omnetpp_r_base.mytest-64 -c General -r 0'),
  ('523.xalancbmk_r', '../run_base_refrate_mytest-64.0000/cpuxalan_r_base.mytest-64 -v t5.xml xalanc.xsl', 38),
  ('525.x264_r', '../run_base_refrate_mytest-64.0000/x264_r_base.mytest-64 --pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720', 68),
  ('531.deepsjeng_r', '../run_base_refrate_mytest-64.0000/deepsjeng_r_base.mytest-64 ref.txt', 62),
  ('541.leela_r', '../run_base_refrate_mytest-64.0000/leela_r_base.mytest-64 ref.sgf', 8),
  ('548.exchange2_r', '../run_base_refrate_mytest-64.0000/exchange2_r_base.mytest-64 6', 36),
  ('557.xz_r', '../run_base_refrate_mytest-64.0000/xz_r_base.mytest-64 cld.tar.xz 160 19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474 59796407 61004416 6', 40),
  ('999.specrand_ir', '../run_base_refrate_mytest-64.0000/specrand_ir_base.mytest-64 1255432124 234923', 1)
]

#benchmark_dir_prefix = '/../benchmarks_wombat/benchspec/CPU/'
benchmark_dir_prefix = '/../benchmarks_wombat/benchspec_2/CPU/'
benchmark_dir_postfix = '/run/run_base_refrate_mytest-64.0000'
