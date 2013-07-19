#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       guessing.py
#       
#       Copyright 2011 Wolf Halton <wolf@sourcefreedom.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#		Guess a number

from random import randint

def main():
	print "Enter your name and a guess"
	n = raw_input("enter your name: ")
	guessed(n)
	print "You guessed!!"
	return 0

def guessed(n):
	
	a = randint(1, 100)
	# print a
	t = 1
	give_up = 'n'
	while give_up != 'yes':
		g = input("enter a number: ")
		if g == a:
			print "%s!, You got it right, and only in try number %i, too" % (n, t)
			break
		if g > a:
			if g == a + 1:
				print "you are almost there, %s, keep trying! This is only your %i try" % (n, t)
			elif g >= a + 2 and g <= a +  6:
				print "you are pretty high"
			elif g > a + 6:
				print "%s, you are now at 30,000 ft over Dallas..."
		else:
			print "You are too low %s." % n
			if g == a - 1:
				print "but you are almost there, %s, keep trying! This is only your %i try." % (n, t)
			elif g <= a - 2 and g >= a -  6:
				print "You have dug a rather deep trench %s, but this is only trial number %i." % (n, t)
			elif g < a - 6:
				print "%s, are you digging a well and forget to mention it?" % (n)
		t = t + 1
	

if __name__ == '__main__':
	main()

