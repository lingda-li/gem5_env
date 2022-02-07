import argparse
import os
import subprocess
from datetime import datetime
#from benchlist_spectest import *
from benchlist_specref_fs import *


parser = argparse.ArgumentParser(description="Run gem5 FS simulation")
parser.add_argument('-c', '--case', required=True)
parser.add_argument('-t', '--trace-dir', default='')
parser.add_argument('cfgs', nargs='*')
args = parser.parse_args()

cwd = os.getcwd()
gem5_dir = cwd + '/../gem5'
gem5_bin = cwd + '/bin/gem5.run1'
#gem5_bin = gem5_dir + '/build/ARM/gem5.opt'
config_file = gem5_dir + '/configs/example/arm/fs_bigLITTLE.py'

log_name = cwd + '/log/' + args.case + '_' + datetime.now().strftime("%m%d%y") + '.log'
with open(log_name, 'w') as log_file:
  print('Write log to', log_name)
  for name, simpoint in benchmark_list:
    log_file.write('********** ' + name + ' **********\n')
    log_file.flush()
    res_dir = cwd + '/res/' + args.case + '/' + name
    gem5_cmd = [gem5_bin, '-d', res_dir, config_file]
    boot_script = 'boot/' + name + '.ref.vl64.rcS'
    gem5_cmd.extend(['--kernel', 'vmlinux.4.15_64', '--dtb', 'armv8_gem5_v1_1cpu.dtb', '--disk', 'aarch64-ubuntu-trusty-headless.img', '--bootscript', boot_script, '--bootloader', '../gem5/system/arm/bootloader/arm64/boot.arm64'])
    gem5_cmd.append('--restore-from')
    gem5_cmd.append(cwd + '/res/at.ref/' + name + '/cpt')
    # Take checkpoints.
    gem5_cmd.append('--maxinsts')
    gem5_cmd.append(str(simpoint * 100000000))
    for cfg in args.cfgs:
      cfg = cfg.replace('\'', '')
      cfg = cfg.replace('\"', '')
      cfg = cfg.replace(' ', '')
      gem5_cmd.append(cfg)
    print(gem5_cmd)
    process = subprocess.call(gem5_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
    if args.trace_dir != '':
      log_file.write('********** scp traces **********\n')
      log_file.flush()
      trace_dir = 'hpc1:/lfs1/work/lli/trace_' + args.trace_dir + '/'
      scp_cmd = ['scp', 'trace.txt', trace_dir + name + '.txt']
      process = subprocess.call(scp_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
      scp_cmd = ['scp', 'sq.trace.txt', trace_dir + name + '.sq.txt']
      process = subprocess.call(scp_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
      rm_cmd = ['rm', '-f', 'trace.txt', 'sq.trace.txt']
      process = subprocess.call(rm_cmd, stdout=log_file, stderr=log_file, universal_newlines=True)
    log_file.flush()
