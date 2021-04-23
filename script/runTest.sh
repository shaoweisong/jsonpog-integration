#!/bin/bash
for i in $(find POG -name *.json); do # Whitespace-safe but not recursive.
    DIFF="$(cmp --silent cms-nanoAOD-repo/$i $i; echo $?)"
    correction validate --version 2 $i
    if [[ $DIFF -ne 0 ]]; then
        echo "There are changes in "$i" wrt cms-nanoAOD/jsonpog-integration.git. "
        echo "-------------- summary - original version -----------------------------------"
        correction summary cms-nanoAOD-repo/$i
        echo "-------------- summary - new version ----------------------------------------"
        correction summary $i
        echo "-------------- differences in summary ---------------------------------------"
        correction summary cms-nanoAOD-repo/$i | grep -v "Corrections in file" > tmp1.txt 
        correction summary $i | grep -v "Corrections in file" > tmp2.txt
        git diff --no-index tmp1.txt tmp2.txt
        echo "-------------- differences in file ----------------------------------------"
        git diff --no-index cms-nanoAOD-repo/$i $i
        echo "----------------------------------------------------------------------------"
    else
        echo "No changes in "$i" wrt cms-nanoAOD/jsonpog-integration.git. "
    fi
done
