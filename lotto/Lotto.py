#!/usr/bin/env python
# Lotto.py
import random
import time

def main():
    choice = 0
    
    while choice != 10:
        randpick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 56]
        time.sleep(.6)
        print ""
        print "_________Main Menu_________"
        print "For Mega-Millions | type  1"
        print "For Powerball     | type  2"
        print "For Pick Three    | type  3"
        print "For Pick Four     | type  4"
        print "For Pick Five     | type  5"
        print "For Fantasy Five  | type  9"
        print "To quit           | type 10"
        print "\n\n"

        choice = input("Enter your choice: ") # or choice = raw_input("Enter your choice: ")
        randpick = [1, 2, 3, 4, 5, 9]
        
        print "Your choice was %d" % (choice)
        if choice == 1:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! Your guaranteed MegaMillions numbers are..."
            time.sleep(3)
            lotto()
            print "\n======================================="
        elif choice == 2:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! This may take a couple of minutes..."
            time.sleep(3)
            PBall()
        elif choice == 3:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! Your guaranteed numbers are..."
            time.sleep(3)
            Pik3()
        elif choice == 4:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! Your guaranteed numbers are..."
            time.sleep(3)
            Pik4()
        elif choice == 5:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! Your guaranteed numbers are..."
            time.sleep(3)
            Pik5()
        elif choice == 6:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! Your guaranteed numbers are..."
            time.sleep(3)
            randpick, choice = Random(randpick, choice)
        elif choice == 7:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "uh-oh! there has been a problem..."
            time.sleep(3)
            randpick, choice = Random(randpick, choice)
        elif choice == 8:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "uh-oh! there has been a problem..."
            time.sleep(3)
            randpick, choice = Random(randpick, choice)
        elif choice == 9:
            bar = []
            for i in range(8):
                bar.append("=")
                print bar
                time.sleep(1)
            print "\n======================================="
            print "Good Luck! Your guaranteed numbers are..."
            time.sleep(3)
            Fantasy5()

        elif choice > 10:
            time.sleep(1)
            print "\n======================================="
            print "I cannot understand your response.  Try again"
            time.sleep(3)
            


def testing(w, t):
    tested = []
    L = 0
    # print tested
    while L < w:
        n = random.randint(1, t)
        if n not in tested:
            tested.append(n)
            L = len(tested)
    return tested
    

def PBall():
    tested = []
    w = 5
    t = 60
    tested = testing(w, t)
    pb = random.randint(1, 40)
    print tested, "is your number set and"
    time.sleep(3)
    print pb, "is your PowerBall"
    
def lotto():
    tested = []
    w = 6
    t = 57
    tested = testing(w, t)
    print  tested

def Pik3():
    tested = []
    for i in range(3):
        j = random.randint(0, 9)
        tested.append(j)
        time.sleep(.5)
        print tested
    
def Pik4():
    tested = []
    for i in range(4):
        j = random.randint(0, 9)
        tested.append(j)
        time.sleep(.5)
        print tested

def Pik5():
    tested = []
    for i in range(5):
        j = random.randint(0, 9)
        tested.append(j)
        time.sleep(.5)
        print tested

def Fantasy5():
    tested = []
    w = 5
    t = 57
    tested = testing(w, t)
    print  tested

def Random(randpick, choice):
    print "... Since you chose a game that hasn't been \nprogrammed yet, here is a random set for you."
    print "We aim to please.  You aim too, please."
    tested = []
    w = random.randint(3,16)
    t = 99
    tested = testing(w, t)
    print  tested
    print "We aim to please.  You aim too, please."
    return (randpick, choice)

main()
