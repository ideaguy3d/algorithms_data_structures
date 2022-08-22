per='Perceptron'
comp1=`cat f2.txt | grep '[ap]' | wc -l`
date_comp="Today's date is `date`"
date_comp2="Today's date is $(date)"
model1=87.65
model2=89.20
echo "Total model accuracy = $(echo "$model1+$model2" | bc)"
echo "Machine Learning model avgerage = $(echo "($model1+$model2)/2" | bc)"
echo $comp1
echo $date_comp
echo $date_comp2
cep="$per Model"
echo "$cep $comp1 for Machine Learning."