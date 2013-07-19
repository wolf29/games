#!/usr/bin/python
# sort things
# make list of random numbers
import random, time
def main():
	choice = 100
	while choice != 99:
		ping = []
		print '''                Enter the process you would like to do 
		by its index number.  For instance, if you want
		to develop a set of random numbers and you want to 
		then sort them from lowest to highest, you would type a '
		1' in the choice box below.
		_____________________________________________________
		
		1 == Sort a random list of numbers from low to high
		2 == Sort a random list of numbers from high to low
		3 == Change an Arabic numeral to a Roman numeral
		4 == not invented yet
		... and so on ...
		99 == quit\n'''
		choice = input("                enter your choice, please =>  ")
		if choice == 1:
			print "    Enter top end of the range of random number choices you like"
			te = input("    Enter the randomizing number you want =>  ") 
			nu = 1 + input("    Enter the quantity of numbers you want to sort=>  ") 
			print "    Your range is 1 - %d and you want to sort %d numbers\n                    Here goes nothing" % (te, nu-1)
			te, nu, ping = pack(te, nu, ping) 
			print "                ", ping, " Raw list"
			ping = srt(ping)
			print "                ", ping, " Sorted list\n"
		if choice == 2:
			print "    Enter top end of the range of random number choices you like"
			te = input("    Enter the randomizing number you want =>  ") 
			nu = 1 + input("    Enter the quantity of numbers you want to sort=>  ") 
			print "    Your range is 1 - %d and you want to sort %d numbers\n                    Here goes nothing" % (te, nu-1)
			te, nu, ping = pack(te, nu, ping) 
			print "                ", ping, " Raw list"
			ping = hsrt(ping)
			print "                ", ping, " Sorted list\n"
		elif choice == 99:
			print "thanks for playing"
			time.sleep(7)
			exit()
	
def pack(te, nu, ping):
	#print "Inside pack(), your range is 1 - %d and you want to sort %d numbers\nHere goes nothing" % (te, nu-1)
	for i in range(nu-1):
		ping.append(random.randint(1,te))
	
	#print ping
	return te, nu, ping

def srt(ping):
	gr = len(ping)
	#print gr, "number of index places"
	#print ping, " Inside sort"
	k = 0
	while k < gr:
	#for k in range(0, gr-1):
		swap_test = False
		#print k, gr, "k and gr in first range", ping
		for i in range(0, gr-1):
			#print i, "and", k, " --i and k as seen in second range"
			#print ping
			if ping[i] > ping[i + 1]:
				a = ping[i]; b = ping[i + 1]
				ping[i], ping[i + 1] = b, a #swap the values 
				#print a, b, "this is the set being sorted"
				#print ping, "is now changed"
				swap_test = True
		k = k + 1
		#print k, "-- This is the count amount"
		#print ping, "This is interior sort"
		if swap_test == False:
			break
	return ping

def hsrt(ping):
	gr = len(ping)
	#print gr, "number of index places"
	#print ping, " Inside sort"
	k = 0
	while k < gr:
	#for k in range(0, gr-1):
		swap_test = False
		#print k, gr, "k and gr in first range", ping
		for i in range(0, gr-1):
			#print i, "and", k, " --i and k as seen in second range"
			#print ping
			if ping[i] < ping[i + 1]:
				a = ping[i]; b = ping[i + 1]
				ping[i], ping[i + 1] = b, a #swap the values 
				#print a, b, "this is the set being sorted"
				#print ping, "is now changed"
				swap_test = True
		k = k + 1
		#print k, "-- This is the count amount"
		#print ping, "This is interior sort"
		if swap_test == False:
			break
	return ping

if __name__ == "__main__":
	main()
