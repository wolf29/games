#!/bin/sh
# www.calpoly.edu/~rasplund/script.html
# DOS interpreter. Impersonates DOS as follows:
# DOS command   Linux equivalent   Action
# cd            cd                Change directory
# dir           ls                List directory contents
# type          cat               List file contents
# del           rm                Delete a file
# ren           mv                Rename a file
# copy          cp                Copy a file

echo "Welcome to the DOS interpreter"
echo "DOS command   Linux equivalent   Action"
echo "cd            cd                Change directory"
echo "dir           ls                List directory contents"
echo "type          cat               List file contents"
echo "del           rm                Delete a file"
echo "ren           mv                Rename a file"
echo "copy          cp                Copy a file"
echo "            Type Ctrl-C to exit"

# Infinite loop
while [ "forever" ]
do
# Show DOS prompt; 
  echo "DOS>  \c"   # '\c' stops an automatic new line
# Read in user's command
  read command arg1 arg2
# Do a Linux command corresponding to the DOS command
  case $command in
    cd)
      cd $arg1
      ;;
    dir)
      ls
      ;;
    type)
      cat $arg1
      ;;
    del)
      rm $arg1
      ;;
    ren)
      mv $arg1 $arg2
      ;;
    copy)
      cp $arg1 $arg2
      ;;
    *)
      echo "DOS does not recognize the command $command"
      ;;
  esac   
done
