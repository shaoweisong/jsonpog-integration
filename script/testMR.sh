#!/bin/bash
NOCHANGED_FILES=()
ADDED_FILES=()
CHANGED_FILES=()
CHANGE_REPORT=./change_report.log
BROKEN_FILES=()

HEAD=$1  # path to the merge request
MASTER=$2  # path to the clean clone

STATUS=0

function validate() {
    VALIDATION=$(correction validate --version 2 $1)
    if [[ $? -ne 0 ]]; then
        echo
        echo "######### VADLIATION ERROR in $1 #########"
        echo ${VALIDATION}
        echo "#################################################################"
        echo
        BROKEN_FILES+=($1)
        STATUS=1
        return 1
    fi
    return 0
}

for i in $(find ${HEAD}/POG -name "*.json*"); do
    if [[ -s ${MASTER}/$i ]]; then
        # file already exists in master
        if cmp --silent ${MASTER}/$i $i; then
            echo "There are changes in $i wrt cms-nanoAOD/jsonpog-integration.git. "
            if validate $i; then
                script/compareFiles.py ${MASTER}/$i $i 2>&1 >> ${CHANGE_REPORT}
                if [[ $? -ne 0 ]]; then
                    echo
                    echo "######### COMPARISON ERROR in $i #########"
                    echo ${CHANGE_SUMMARY}
                    echo "#################################################################"
                    echo
                    BROKEN_FILES+=($1)
                    STATUS=1
                else
                    CHANGED_FILES+=($i)
                fi
            fi
        else
            echo "No changes in "$i" wrt cms-nanoAOD/jsonpog-integration.git. "
            NOCHANGED_FILES+=($i)
        fi
    else
        echo "New file found in $i"
        if validate $i; then
            echo "-------------- summary of new file -----------------------------------"
            correction summary $i
            echo "----------------------------------------------------------------------------"
            ADDED_FILES+=($i)
        fi
    fi
done

echo
if (( ${#CHANGED_FILES[@]} )); then
    echo "Files changed (tests passed): ${CHANGED_FILES[@]}\n"
else
    echo "No files changed.\n"
fi

if (( ${#ADDED_FILES[@]} )); then
    echo "Files added (tests passed): ${ADDED_FILES[@]}\n"
else
    echo "No files added.\n"
fi

if (( ${#BROKEN_FILES[@]} )); then
    echo "Broken files: ${BROKEN_FILES[@]}\n"
else
    echo "No broken files.\n"
fi

echo "Done."

exit ${STATUS}
