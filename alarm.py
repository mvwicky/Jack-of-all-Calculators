import os
import time


when = raw_input("How many minutes?")
when = (float(when) * 60)
start_time = time.clock()
while (start_time + when) > time.clock():
	print "Waiting..."
	print int(time.clock())
	time.sleep(1)
if (start_time + when) <= time.clock():
	print int(time.clock())
	print "Done"
