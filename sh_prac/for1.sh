
x=1
while [ $x -lt 3 ];
do 
    echo "while $x"
    ((x+=1))
done 

echo '--'

for x in {1..5..2}
do 
    echo $x
done 

echo '--'

for ((x=2;x<=4;x+=2))
do
    echo $x
done 

echo '--'

for temp in temps/*
do 
    echo $temp 
done 

echo '--'

for book in $(ls books/ | grep -i 'air')
do
    echo $book 
done 


# eof #