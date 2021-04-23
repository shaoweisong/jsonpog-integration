for i in $(find POG -name *.json); do # Whitespace-safe but not recursive.
    DIFF="$(cmp --silent cms-nanoAOD-repo/$i $i; echo $?)"
    correction validate --version 2
    if [[ $DIFF -ne 0 ]]; then
        echo "There are changes in "$i" wrt cms-nanoAOD/jsonpog-integration.git. "
        echo "-------------- original version -----------------------------------"
        correction summary cms-nanoAOD-repo/$i
        echo "-------------- new version ----------------------------------------"
        correction summary $i
        echo "-------------- diff version ----------------------------------------"
        correction summary cms-nanoAOD-repo/$i > tmp1.txt
        correction summary $i > tmp2.txt
        git diff --no-index tmp1.txt tmp2.txt
    else
        echo "There is no changes in "$i" wrt cms-nanoAOD/jsonpog-integration.git. "
    fi
