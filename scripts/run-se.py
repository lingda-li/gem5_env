import argparse
import os
import subprocess
import importlib
from datetime import datetime


parser = argparse.ArgumentParser(description="Run gem5 SE simulation")
parser.add_argument('-c', '--case', required=True)
parser.add_argument('-b', '--benchmarks', required=True)
parser.add_argument('-t', '--trace-dir', default='')
parser.add_argument('-l', '--load-checkpoints', action='store_true')
parser.add_argument('-r', '--read-config', default='')
parser.add_argument('cfgs', nargs='*')
args = parser.parse_args()

cwd = os.getcwd()
gem5_dir = cwd + '/../gem5'
gem5_bin = cwd + '/bin/gem5.run'
#gem5_bin = gem5_dir + '/build/ARM/gem5.opt'
if args.read_config == '':
  config_file = gem5_dir + '/configs/example/arm/starter_se.py'
else:
  config_file = gem5_dir + '/configs/example/read_config.py'
  config_dir = cwd + '/../../PerfVec/g5_res/'
#benchlist = "benchlist_spectest_" + args.benchmarks
benchlist = "benchlist_" + args.benchmarks
#trace_root_dir = 'hpc1:/lfs1/work/lli/trace_'
#trace_root_dir = 'lld@acl01.csi.bnl.gov:/data1/lld/t2v/trace_'
#trace_root_dir = '/data/lli/pr_1023/trace_'
trace_root_dir = '/data1/lld/t2v/trace_'
bl = importlib.import_module(benchlist)

log_name = cwd + '/log/' + args.case + '_' + args.benchmarks + '_' + datetime.now().strftime("%m%d%y") + '.log'
with open(log_name, 'w') as log_file:
  print('Write log to', log_name)
  #for name, cmd, simpoint in benchmark_list:
  for name, cmd in bl.benchmark_list:
    log_file.write('********** ' + name + ' **********\n')
    log_file.flush()
    benchmark_dir = cwd + bl.benchmark_dir_prefix + name + bl.benchmark_dir_postfix
    os.chdir(benchmark_dir)
    res_dir = cwd + '/res/' + args.case + '/' + name
    gem5_cmd = [gem5_bin, '-d', res_dir, config_file]
    if args.read_config != '':
      # Fix the path in the old config file
      config_path = config_dir + args.read_config + '/' + name + '/'
      with open(config_path + 'config.ini', 'r', encoding='utf-8') as src, \
           open(config_path + 'config.new.ini', 'w', encoding='utf-8') as dst:
        for line in src:
          if 'cwd=' in line:
            line = 'cwd=' + os.getcwd() + '\n'
          dst.write(line)
      gem5_cmd.append(config_dir + args.read_config + '/' + name + '/config.new.ini')
    if args.load_checkpoints:
      gem5_cmd.append('--restore')
      gem5_cmd.append(cwd + '/res/se.ref.at.sp100m.10b.cp/' + name + '/cpt')
    for cfg in args.cfgs:
      cfg = cfg.replace('\'', '')
      cfg = cfg.replace('\"', '')
      cfg = cfg.replace(' ', '')
      gem5_cmd.append(cfg)
    if args.read_config == '':
      gem5_cmd.append(cmd)
    print(*gem5_cmd)
    process = subprocess.call(gem5_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
    if args.trace_dir != '':
      log_file.write('********** scp traces **********\n')
      log_file.flush()
      trace_dir = trace_root_dir + args.trace_dir + '/'
      scp_cmd = ['scp', 'trace.txt', trace_dir + name + '.txt']
      process = subprocess.call(scp_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
      if os.path.exists('sq.trace.txt'):
        log_file.write('********** scp sq traces **********\n')
        scp_cmd = ['scp', 'sq.trace.txt', trace_dir + name + '.sq.txt']
        process = subprocess.call(scp_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
    rm_cmd = ['rm', '-f', 'trace.txt']
    process = subprocess.call(rm_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
    if os.path.exists('sq.trace.txt'):
      rm_cmd = ['rm', '-f', 'sq.trace.txt']
      process = subprocess.call(rm_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
    log_file.flush()
