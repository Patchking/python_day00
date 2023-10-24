#!/bin/bash

echo "Testing test..."
echo 

while IFS= read -r line 
do
    echo "$line"
    python3.11 ../main.py "$line"
    echo
done < "test"