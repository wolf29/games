#!/usr/bin/env python
# Welcome in 2 ways
# Wolf Halton wolf@sourcefreedom.com
from turtle import *

def main():
    #function call, or module call
    Welcome()
def Welcome():
    name = raw_input("Enter your Name: ")
    print "Welcome to the Zoo, ", name
    turtlebox()
def turtlebox():
    reset()
    circle(59)
    reset()
    turtledemo()
main()
    
