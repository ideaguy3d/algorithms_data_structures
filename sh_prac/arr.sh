a1=(1 2 3 4)
a1+=(5 6 7)
echo ${a1[@]}
echo ${a1[@]:2:4}
echo "The 4th elem = ${a1[3]}"

# declare -A city_details
# city_details=([city_name]="New York" [city_population]=14000000)
# # remember to use "!" to get all the keys
# echo ${!city_details[@]} "Data in city"
# echo "${city_details[city_name]} has ${city_details[city_population]}"

# Create empty associative array
declare -A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn tree"
model_metrics[model_f1]=0.82

echo "Machine Learning model name = $model_metrics[model_name]"
# echo ${!model_metrics[@]}





# end of file #
