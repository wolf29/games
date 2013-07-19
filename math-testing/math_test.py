#!/usr/bin/env python
# math_test.py
# 
from random import randint
importfile maths.txt


def main():
	name = "name"
	operand1 = 0
	operand2 = 0
	score = 0
	d = 3 
	
	while d != 7:
		print '''menu
		if you would like to take the awful test, press 1
		if you would like to quit,                press 7
		'''
		d = input("Enter your choice: ")
		print "Score is %i" % score
		if d == 1:
			print "Here we go now"
			name = Name(name)
			#print name, "on line 23"
			operand1, operand2 = rands(operand1, operand2)
			score, operand1, operand2 = questions(score, operand1, operand2)



def Name(name):
	name = raw_input("enter your name ")
	print "Welcome %s! Glad to see you" % (name)
	return name

def rands(operand1, operand2):
	operand1 = randint(1, 500)
	operand2 = randint(1, 500)
	return (operand1, operand2)

def questions(score, operand1, operand2):
	for i in range(10):
		operand1, operand2 = rands(operand1, operand2)
		sum = operand1 + operand2
		print "%i + %i = ______" % (operand1, operand2)
		summ = input("What is the answer? ")
		if sum == summ:
			print "Great job! %i + %i equals %i!\n" % (operand1, operand2, sum)
			score = score + 1
		else:
			print "Sorry, %i + %i equals %i!" % (operand1, operand2, sum)
		print "Your score is %i." % score
	return (score, operand1, operand2)

# call main()
main()
