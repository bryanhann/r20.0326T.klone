import os
import sys

SEP      = os.sep
NIL      = ''
THIS     = os.path.realpath( sys.argv[0] )
NAME     = os.path.basename( THIS )
HERE     = os.path.split(THIS)[0]
HOME     = os.environ['HOME']
LOCAL    = HOME  + SEP + '.local'
CACHE    = HOME  + SEP + '.cache'
MY       = HERE  + SEP + 'my'
MANPAGE  = MY    + SEP + 'manpage'

def slurp(fname):
     with open(fname) as fd:
         return fd.read()

def manpage():
    return slurp(MANPAGE)
