#!/bin/bash

echo "Testing test..."
cat test
echo
echo
echo "Printed part"
cat test | python3.11 ../main.py 10
echo

