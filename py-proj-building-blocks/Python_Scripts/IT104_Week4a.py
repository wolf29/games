#!/usr/env python
# Lift Ticket Printer
# Wolf Halton wolf@soucefreedom
print "Lift Ticket Printer"
Date = raw_input("Enter Date, mm-dd-yyyy: ")
FirstName = raw_input("Enter your first name: ")
LastName = raw_input("Enter Your Last Name: ")
Age = input("Enter your Age: ")
print """=============
Slope Menu
Bunny Slope = 1
Average Slope = 2
Insane Slope = 3
================="""
slope = input("Enter Your Choice of Slope: ")

print "You Entered ", FirstName, " ", LastName
print "Your age is: ", Age

if Age < 18:
    print "You are Prohibited.  Please enter a \
choice of 1 or 2"
    slope = input("Enter 1 or 2: ")

if slope == 1:
    print "BUNNY SLOPE (1)"
elif slope == 2:
    print "AVERAGE SLOPE (2)"
elif slope == 3:
    print "SUICIDAL INSANITY SLOPE (3)"
print FirstName, LastName
print Date
    
    
