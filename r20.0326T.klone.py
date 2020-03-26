#!/usr/bin/python

from  my.std import *
from  shutil  import rmtree as __rmtree
from  os.path import isdir
from  my.env     import dCUT
from  my.stuff   import __klone
from  my.stuff   import dump, kache4src
from  my.parser  import parser
import sys
out = sys.stdout.write
err = sys.stderr.write
o=parser.parse_args()

o.m         and exit(out(slurp(MANPAGE)))
o.l         and exit(dump())
o.c in dCUT  or  exit('-p option not found')
o.src          or  exit('src is missing')

src = dCUT[o.c] + o.src
dst = o.dst
new = o.z
kache = kache4src(src)

new          and __rmtree(kache, ignore_errors=True)
isdir(kache) or  __klone(src,kache)
isdir(kache) or  exit( 'could not write cache' )
dst          or  exit()
isdir(dst)   and exit ('dst already exists')
True         and __klone(kache,dst)
isdir(dst)   or  exit ('dst error')

