#!/bin/sh
'''exec' C:/Anaconda3/envs/fastai2/bin/python "$0" "$@"
' '''
# -*- coding: utf-8 -*-
import re
import sys
from nbdev.cli import nbdev_install_git_hooks
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(nbdev_install_git_hooks())
