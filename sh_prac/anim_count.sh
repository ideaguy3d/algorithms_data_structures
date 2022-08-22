#!/bin/bash

echo "Animal Counts:"
cat animals.csv | cut -d " " -f 2 | sort | uniq -c 
