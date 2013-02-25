
amount = float(raw_input("->"))
#print(amount)
d = int(amount)
d = float(d)
lod = amount - d
#print(lod)
if (lod / .25 < 1):
	amountOfQuarters = 0;
if (lod / .25 >= 1):
	amountOfQuarters = int(lod/.25)
print "Quarters =" , amountOfQuarters
lod = lod - (amountOfQuarters * .25)
if (lod / .1 < 1):
	amountOfDimes = 0;
if (lod / .1 >= 1):
	amountOfDimes = int(lod/.1)
print "Dimes =" , amountOfDimes
lod = lod - (amountOfDimes * .1)
if (lod / .05 < 1):
	amountOfNickels = 0
if (lod / .05 >= 1):
	amountOfNickels = int(lod/.05)
print "Nickels =" , amountOfNickels
lod = lod - (amountOfNickels * .05)
if (lod / .01 < 1):
	amountOfPennies = 0
if (lod / .01 >= 1):
	amountOfPennies = int(lod/.01)
print "Pennies =" , amountOfPennies
lod = lod - (amountOfPennies * .01)
