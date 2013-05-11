import conversions as c
import misc as m
#import formulas as f
import operations as o

def get_inputs():
	i = [0]
	n = 0
	while i[n] <= "done":
		t = raw_input("->")
		if t == "done" or t == "" or t == " ":
			del i[0]
			break
		t = float(t)
		i.append(t)
		n += 1
	return i

def clear_screen():
	import os
	if os.name == "posix":
		os.system('clear')
	elif os.name in ("nt" , "dos" , "ce"):
		os.system('CLS')
	else:
		print '\n' * 100

print "This is a calculator program"
while 1:
	print "1: Addition"
	print "2: Subtraction"
	print "3: Multiplication"
	print "4: Division"
	c = raw_input("->")
	c = int(c)
	clear_screen()
	if c not in [1 , 2 , 3 , 4]:
		print "Invalid Response"
	elif c in [1 , 2 , 3 , 4]:
		print "Please give inputs"
		print "Type 'done' or nothing to stop"
		opp = o.Operations(get_inputs())
		if c == 1:
			print opp.inputs
			print opp.addition()
		if c == 2:
			print opp.inputs
			print opp.subtraction()
		if c == 3:
			print opp.inputs
			print opp.multiplication()
		if c == 4:
			print opp.inputs
			print opp.division()

