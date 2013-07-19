# -*- coding: utf-8 -*-
from easygui import *
import sys

while 1:
    msgbox('''How Big is Your Monster?
Many children are scared of Giant Bugs.
Dr Physics' Cube-root Calculator
Can Help''')

    msgbox('''Using this simple formula
You can prove that a 12-meter-tall bug
would be harmless.''')
    
    msg = '''Do you want to continue?
This could get a little bit scary.'''
    title = "Please Confirm Your Intention"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel
    image = "bug.gif"
    msgbox('An average bug is about 7 millimeters long, 3 mm wide and 2 mm thick.', image="bug.gif")
    
    errmsg = "moo"
    #while loop to let the user fix missing entries WH
    while errmsg == "moo":
        msg = "How does yours compare to an average bug"
        title = "bug stats"
        fieldNames = ["Length","Width","Thickness"]
        fieldValues = []  # blanks for the values
        fieldValues = multenterbox(msg,title, fieldNames)
        #image = bug.gif
 
        # make sure that none of the fields was left blank
        while 1:    
            if fieldValues == None: 
                break
            errmsg = "moo"
            for i in range(len(fieldNames)):
                errmsg = ""
                if fieldValues[i].strip() == "":
                    errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
            if errmsg == "":
                break # no problems found
            
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        
    print("Reply was: %s" % str(fieldValues))

    x, y, z = fieldValues
    x = int(x); y = int(y); z = int(z);
    #print type(x), type(y), type(z)
    tw = x * y * z
    
    msgbox("Reply was: %s. A bug that size would weigh about %.2f pounds, and would be unable to walk." % (str(fieldValues), tw))

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel
