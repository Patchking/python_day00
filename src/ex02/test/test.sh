#!/bin/bash


for ((i=0; i<=4; i++)); do
    echo "Testing test$i..."
    cat test$i
    echo
    cat test$i | python3.11 ../mfinder.py
    echo
done