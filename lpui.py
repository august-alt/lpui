#! /usr/bin/python3

import re
import subprocess

LOCAL_POLICY_DIR = "/var/cahce/local/policy"

gpuiExecutable = '/usr/bin/gpui-main'
gpuiParameters = ['--path', LOCAL_POLICY_DIR]

wgetPopen = subprocess.Popen([gpuiExecutable] + gpuiParameters,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

wgetPopen.stdout.close()
wgetPopen.wait()
