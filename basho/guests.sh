#!/bin/sh
case "$1" in
  fred)
    echo "Hi fred. Nice to see you"
    ;;
  joe)
    echo "Hi! How are you Joey?"
    ;;
  harry)
    echo "Go away, Harry!  You aren't welcome here"
    ;;
  *)
    echo "Who are you? We don't have a $1 on the guest list here."
    ;;
esac    # This is “Case” spelled backward. Clever lad, that Bourne.
