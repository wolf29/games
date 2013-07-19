#!/bin/sh
# keymaster.sh
password="xul"
answer=""
# Loop around forever (until the break statement is used)
while [ "forever" ]
do
# Ask the user for the password
  echo "I am the gatekeeper.  Are you the keymaster?\nIf you are the Keymaster, enter the key \c"
# Read in what they type, and put in it $answer
  read answer

# If the answer is the password, break out of the while loop
  if [ "$answer" = "$password" ]
  then
    break
  fi
done
# If they get to here, they must really be the keymaster,
# otherwise the script would keep looping
echo "Welcome Keymaster.\nWe must make the way ready for the return of Xul!"

