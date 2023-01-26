
echo "_> file contents"

cat f2.txt 

echo "_> now, the ops"

cat f2.txt | sort | uniq -c | sort | tail -n 3

echo "_> animal types:"

cat animals.csv | cut -d " " -f 2

cat animals.csv | cut -d " " -f 1 1> animal_types2.txt 

n_date="The date&time is `date`"

echo "_> done $n_date"

a1=("per" "cep" "tron")

echo ${a1[2]}

# 