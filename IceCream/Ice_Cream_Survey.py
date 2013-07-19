#!/usr/bin/env python
# -*- coding: utf-8 -*-
# icecream_survey.py
# EasyGUI example
# wolf@sourcefreedom.com
from random import randint
from easygui import *
import sys

while 1:
    msgbox('''Hello, seeker!
There are many flavors of Ice Cream
This survey covers the most popular choices...''')

    msgbox('''Ice cream has a proud heritage, 
going back to the Roman conquest.  
There are many flavors, 
from generic Vanilla 
to exotic Earwax.''')

    msg ="What is your favorite flavor?"
    title = "Ice Cream Survey"
    choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road", "Moose Tracks", "Pistaccio", "EarWax"]
    choice = choicebox(msg, title, choices)
    dex = randint(0, 6)
    print dex, choices[dex], "Alternate choice"
    lex = choices[dex]
    

  # note that we convert choice to string, in case
  # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")
    print choice
    
    msg = "Are you Sure You Wouldn't Rather Have %s Flavor?" % (choices[dex])
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        msgbox("""I am sure you will be happy with
        	succulent, flavourful %s. """ % (lex))
        pass  # user chose Continue
    else:
        msgbox("OK then.  I was just asking...")
        pass

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel
