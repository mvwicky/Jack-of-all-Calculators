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

opp = o.Operations(get_inputs())
print opp.addition()
print opp.subtraction()
print opp.multiplication()
print opp.division()