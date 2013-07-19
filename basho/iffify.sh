#!/bin/sh
# show script
if [ -d $1 ]
then
  ls $1
else
  cat $1
fi

