echo "starting computation..."
cat f2.txt | egrep 'carrot|lime' | sort
cat f2.txt | egrep 'carrot|lime' | wc -l 
echo "computation complete."