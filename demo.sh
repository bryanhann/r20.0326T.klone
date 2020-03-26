here=$(dirname $(grealpath $0))
source $here/demo.config.sh
rm -rf $R20_0326T_CACHE
export KLONE=$here/r20.0326T.klone.py

MAGIC=/tmp/$RANDOM.$RANDOM
mkdir $MAGIC
pushd $MAGIC
log () {
    echo
    echo "======================================================================================================================="
    echo $*
    echo "======================================================================================================================="
}
log " Press enter for demo of [KLONE -cb hardhat foo]" ; read
$KLONE -cb hardhat foo
log " Press enter for demo of [KLONE -cb hardhat bar] which uses now uses the cache" ; read
$KLONE -cb hardhat bar
log "That was quick! Press enter for demo of [KLONE -cb -z hardhat zot] which clears the cache the cache" ; read
$KLONE -cb -z hardhat zot



echo
log "Demos are done. You are being dumped into a shell to with the command."
log "Start with \$KLONE -m to read the man page. When finished, type 'exit' to clean up."
echo
$SHELL
popd
echo Cleaning up.
rm -rf $MAGIC


