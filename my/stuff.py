#!/usr/bin/python

import os
import shutil
import subprocess
from env import KACHE, dCUT

def kache4path(path):
    return '%s/%s.%s' % (KACHE,path, 'tagged')

def path4src(src):
    ii = src.find('//')
    assert ii > 0
    return src[ii+2:]

def kache4src(src):
    return kache4path(path4src(src))

def dump():
    keys = list(filter(None, dCUT.keys()))
    if not keys:
        print( "No current Options for -c." )
    else:
        print( "Options for -c:" )
        for k in keys:
            print "\t-c%s -> prepend your SRC with '%s'" % (k,dCUT[k])

##############################################################################
## Functions starting with __ are considered dangerously impure because
## they have the potential of changing the directory structure or files.
##
## This is a stricter sense of impure that functional programming impurity.
## We do not worry about writing to stdin or stdout, or reading from files.

def __tryklone(src,dst):
    return dst and not os.path.isdir(dst) and __klone(src,dst)

def __spit(path,data):
    with open(path, 'w') as fd: fd.write(data)

def __klone(src,dst):
    return __kall('git clone %s %s' % (src,dst))

def __rmtree(path):
    shutil.rmtree(path, ingore_errors=True)

def __kall(cmd):
    print('>'*20 + cmd)
    return subprocess.call(cmd.split())

