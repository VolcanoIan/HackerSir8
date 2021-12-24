#!/bin/bash
#
# Original code with Python:
# 
# a = int(input('Enter an integer:'))
# b = int(input('Enter an integer:'))
# if a % b == 0:
# 	print('a is a multiple of b')
# else:
# 	print('a is not a multiple of b')
read -p "Enter an integer:" a
read -p "Enter an integer:" b
total=`expr $a % $b`
if test $total = 0
then
	echo "a 是 b 的倍數"
else
	echo "a 不是 b 的倍數"
fi