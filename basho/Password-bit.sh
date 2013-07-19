#!/bin/sh
password="open"
answer=""
# Loop around forever (until the break statement is used)
while [ "forever" ]
do
# Ask the user for the password
  echo "Guess the password to quit the program> \c"
# Read in what they type, and put in it $answer
  read answer

# If the answer is the password, break out of the while loop
  if [ "$answer" = "$password" ]
  then
    break
  fi
done
# If they get to here, they must've guessed the password,
# because otherwise it would just keep looping
echo "Good guess!"

