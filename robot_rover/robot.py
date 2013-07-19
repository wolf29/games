#!/usr/bin/env python
# robot.py
# wolf@sourcefreedom.com

import random

def main():
    fuel = 0
    orient = 1 # degrees on a circle from starting place
    x = 0
    y = 0
    b = 0
    c = 0
    # MAX = 101
    # MIN = -1
    fuel = random_value(fuel)
    choice = 0
    while choice != 4:
        print """
====Menu====
Choose from the following:
to turn, type 1
to move, type 2
to quit, type 4

"""
        choice = input("Enter your choice: ")
        #series of 'if' statements to allow choices
        if choice == 1:
            orient = turn(orient)
        elif choice == 2:
            x, y, fuel, orient = move(x, y, fuel, orient)
            
        print "You have", fuel, "units of fuel."
        print "You are facing", orient, "degrees."
        print "Your location is", x, ", ", y, "on the board."

def turn(orient):
    Or = orient
    ex = raw_input("If you really don't want to turn, type 'x': ")
    if ex == "x":
        print "Ok, you don't have to turn."
    else:
        print "enter your new heading as a positive or negative number" 
        delta = input("enter turn amount in degrees: ")
        Or = Or + delta
    print "your heading is", Or
    orient = Or
    return (orient)
    

def random_value(a):
    a = random.randint(40, 200)
    return (a)

def move(x, y, fuel, orient):
    xx = x
    yy = y
    fuell = fuel
    mv = input("enter move in kilometers: ")
    MAX = 101
    MIN = -1
    if mv <= fuell:
        xx = xx + mv
        fuell = fuell - mv
    else:
        print "You have made a wise decision to stand still"

    fuel = fuell
    x = xx
    y = yy

    return (x, y, fuel, orient)
    

main()
