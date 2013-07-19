#!/bin/sh
# until-E.sh
# Start at hotdog 1
hotdog=1
until [ $hotdog -eq 13 ] # -eq is "equal to"
do                       # signals the start of the body of the loop 
# Print out the hotdog eaten
  echo "Hotdog no. $hotdog"
# Add one to the number of hotdogs eaten
  hotdog=`expr $hotdog + 1`  #  This is also called an incrementer statement
done                     # signals the end of the body of the loop

echo "\nFinished"       # 'backslash n (\n) makes a line return
echo "Man, I'm full.  I ate almost $hotdog hotdogs!" 
