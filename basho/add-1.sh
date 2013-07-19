#!/bin/sh
for result in [$1 $2 $3 $4]
do
result=`expr $result + 1`
echo "Result is $result"
done
#add 1
