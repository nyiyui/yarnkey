#!/bin/sh

printf 'destination path: '
read -r dest

cp *.py $dest
cp -r lib $dest
(cd $dest && echo "copied on $(date -Ins)" > meta.txt)
