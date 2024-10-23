#!/bin/bash 
num1=$1
num2=$2
num3=$3 

sum=$((num1 + num2))
echo "the sum of $num1 and $num2 is: $sum"

product=$((sum * num3)) 
echo "the multiplication of $sum by $num3 is: $product"