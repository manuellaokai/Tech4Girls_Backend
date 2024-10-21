#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <First Name> <Last Name>"
    exit 1
fi 

first_name=$1
last_name=$2
echo "Hello, $first_name $last_name! Welcome to Bash scripting."
