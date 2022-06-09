#! /usr/bin/python3

import re
import subprocess

LOCAL_POLICY_DIR = '/var/cache/gpupdate/local_admin_policy'

gpuiExecutable = '/usr/bin/gpui-main'
gpuiParameters = ['-p', LOCAL_POLICY_DIR]

gpuiProcess = subprocess.call([gpuiExecutable] + gpuiParameters,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)

gpuiProcess.stdout.close()
gpuiProcess.wait()
