#!/bin/bash

echo "Testing test0..."
cat test0
echo
cat test0 | python3.11 ../mfinder.py
echo
echo "Testing test1..."
cat test1
echo
cat test1 | python3.11 ../mfinder.py
echo
echo "Testing test2..."
cat test2
echo
cat test2 | python3.11 ../mfinder.py
echo