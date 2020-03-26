import argparse
parser=argparse.ArgumentParser()

parser.add_argument(
    '-m'
    , action ='store_true'
    , help='Show man page.'
)
parser.add_argument(
    '-l'
    , action ='store_true'
    , help='List installed shortcuts.'
)
parser.add_argument(
    '-z'
    , action ='store_true'
    , help="clear the cache before cloning. ('zero' it.)"
)
parser.add_argument(
    '-c'
    , action ='store'
    , metavar='CUT'
    , default=''
    , help='use a shortcut. Prepend src with prefix keyed to CUT'
)
parser.add_argument(
    'src'
    , help='the url of a remote git repository'
    , nargs='?'
)
parser.add_argument(
    'dst'
    , nargs='?'
    , help='the location you would like to clone to'
)


