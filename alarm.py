import os
import time

waiting = ["W" , "a" , "i" , "t" , "i" , "n" , "g" , "." , "." , "."]

def alarm(t): # t in minutes
	t = (float(t) * 60)
	s = time.clock()
	n = 0
	while (s + t) > time.clock():
		print waiting[n] ,
		n += 1
		time.sleep(3)
		if n == 10:
			n = 0
			print " "
	if (s + t) <= time.clock():
		print "Done" 

the_time = raw_input("Time until alarm goes->")
alarm(the_time)