#! /bin/bash

arr=("classical-cipher" "symmetric-key-encryption")
for s in ${arr[@]}
do
    git remote add ${s} ../${s}
    git fetch ${s}

    git read-tree --prefix=${s}/ ${s}/master

    git checkout -- .
    git add .
    git commit -m 'add ${s}'

    git merge -s subtree ${s}/master --allow-unrelated-histories
done
