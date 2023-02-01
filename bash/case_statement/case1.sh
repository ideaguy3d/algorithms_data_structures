echo "checking $1"

version_to_do='if'

if [[ $version_to_do='if' ]]; then 
    echo 'invoking "if" code:'
    if grep -q 'sydney' $1; then 
        mv $1 sydney/ 
    fi
    if grep -q 'melbourne|brisbane' $1; then 
        rm $1
    fi
    if grep -q 'canberra' $1; then
        mv $1 "IMPORTANT_$1"
    fi
fi 

# - if version -
if [[ $version_to_do='case' ]]; then
    echo 'invoking "case" code:'

    # - case version -
    case $(cat $1) in 
        *sydney*)
        mv $1 sydney/ ;; 
        *melbourne*|*brisbane*)
        rm $1 ;; 
        *canberra*)
        mv $1 "IMPORTANT_$1" ;; 
        *)
        echo "No cities found" ;; 
    esac

fi 





# eof 
