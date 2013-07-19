#!/bin/bash

#  'echo' is fine for printing single line messages,
#+  but somewhat problematic for for message blocks.
#   A 'cat' here document overcomes this limitation.

#cat fibo.sh
#cat <<End-of-message
#-------------------------------------
#This is line 1 of the message.
#This is line 2 of the message.
#This is line 3 of the message.
#This is line 4 of the message.
#This is the last line of the message.
#First I read in another file and then and EOM file
#-------------------------------------
# End-of-message

cd /etc
grep wolf passwd  
VAR1=12
echo $VAR1

# Check for the word "and" in a file
result=`grep $1 $2`
if [ "$result" ]
then
  echo "The file $2 includes the word $1"
fi


#  Replacing line 7, above, with
#+   cat > $Newfile <<End-of-message
#+       ^^^^^^^^^^
#+ writes the output to the file $Newfile, rather than to stdout.

exit


