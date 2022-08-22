x="king"

if [ $x="king" ]; then
    echo "sir $x!"
else
    echo "yes queen"
fi

v=5

if [ $v -gt 4 ]; then
    echo "Expert Level"
else 
    echo "non expert"
fi 


# chaining AND && or OR ||
x=10

if [[ $x -ge 10 && $x -lt 11 ]]; then 
    echo "x is greater than or equal to 10 and less than 11"
else 
    echo "x is not it"
fi 

if grep -q Hello words.txt; then 
    echo "... well Hello!"
fi

date > cur_date.txt 

echo '--'

if $(grep -q Aug cur_date.txt); then 
    echo "We're in August"
else 
    echo "we are not in August"
fi




# eof # 