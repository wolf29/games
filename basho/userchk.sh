#!/bin/sh
# userchk.sh 
# Check for a supplied user in the /etc/passwd file
cd /etc
result=`grep $1 passwd`
if [ "$result" ]
then
  echo "The username $1 exists.  Choose an alternate username."
fi


