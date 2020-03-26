import os
import sys
from util import extract
from std import *

pR20 = 'R20_0326T_'
pCUT = 'R20_0326T_CUT_'

dR20    = extract( pR20, os.environ)
dCUT    = extract( pCUT, os.environ)

try:
    KACHE=dR20['CACHE']
except KeyError:
    exit ('bad environment variable')

for key in dCUT:
    dCUT[ key ]=dCUT[key] + '/';
dCUT[ NIL ] = NIL

