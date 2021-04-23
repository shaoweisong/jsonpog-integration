#!/bin/bash
NOCHANGED_FILES=""
CHANGED_FILES=""
BROKEN_FILES=""
for i in $(find POG -name *.json); do # Whitespace-safe but not recursive.
    STATUS="$(correction validate --version 2 $i; echo $?)"
    STATUS=${STATUS: -1}
    if [[ $STATUS -ne 0 ]]; then
        BROKEN_FILES=$BROKEN_FILES"\n"$i
    else
        DIFF="$(cmp --silent cms-nanoAOD-repo/$i $i; echo $?)"
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
            CHANGED_FILES=$CHANGED_FILES"\n"$i
        else
            echo "No changes in "$i" wrt cms-nanoAOD/jsonpog-integration.git. "
            NOCHANGED_FILES=$NOCHANGED_FILES"\n"$i
        fi
    fi
done

echo -e "Good files with no changes:"$NOCHANGED_FILES
echo
echo -e "Good files with changes:"$CHANGED_FILES
echo
if [[ ${#BROKEN_FILES} -ne 0 ]]; then
    echo -e "Broken files:"$BROKEN_FILES
    echo
    exit -1
else
    echo -e "No broken files."
fi
echo "Done."
