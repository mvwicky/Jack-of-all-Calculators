import os

categories = ["Length" , "Mass/Weight" , "Volume" , "Temperature" , "Currency"]

len_units = ["Meters" , "Kilometers" , "Feet" , "Yards" , "Miles"]

mass_units = ["Milligrams" ,  "Grams" , "Kilograms" , "Metric tons" , "Ounces" , 
			  "Pounds" , "Tons" , "Troy Ounces"]

vol_units = ["Teaspoon" , "Milliliter" , "Tablespoon" , "Liter" , "Ounce" , 
	    	 "Cubic Meter" , "Pint" , "Quart" , "Gallon"]

tem_units = ["Farenheit" , "Celsius" , "Kelvin" , "Rankine" , "Delisle" , "Newton"]

currencies = ["USD" , "EUR" , "GBP" , "CAD" , "JPY", "CNY"]

len_to = [ [.001 , 3.28084 , 1.09361 , .000621371] ,
		   [ 1000 , 3280.84 , 1093.61 , .621371] , 
		   [  .3048 , .0003048 , .3333333 , .000189394] ,
		   [.9144 , .0009144 , 3 , .000568182] ,
		   [1609.34 , 1.60934 , 5280 , 17] ]


mass_to = [[ .001 , .00001 , .00000001 , .000035274 , .0000022046 , .0000000011023 , .000321507466 ] ,
		   [1000 , .001 , .000001 , .035274 , .00220463 , .0000011023 , .0321507466 ] ,
		   [100000 , 1000 , .001 , 35.274 , 2.20462 , .00110231 , 32.1507466 ] ,
		   [1000000000 , 100000 , 1000 , 35274 , 2204.62 , 1.10231 , 32150.7466] ,
		   [28349.5 , 28.3495 , .0283495 , .00002835 , .0625 , .00003125 , .911458333] ,
		   [453492 , 453.592 , .453592 , .000453592 , 16 , .0005 , 14.5833333 ] ,
		   [907200000 , 907185 , 907.185 , .907185 , 32000 , 2000 , 29166.6667 ] ,
		   [31103.4768 , 31.1034768 , .0311034768 , .0000311034768 , 1.09714286 , .0685714286 , .0000342857143]
			]

vol_to = [[4.92892 , .3333333 , .00492892 , .1666667 , .0000049289 , .0104167 , .00520833 , .00130208] ,
		  [.202884 , .067628 , .001 , .033814 , .000001 , .00211338 , .00105669 , .000264172] ,
		  [3 , 14.7868 , .0147868 , .5 , .000014787 , .03125 , .015625 , .00390625] ,
		  [202.884 , 4.92892 , 	.333333333 , .16666666 , .0000049289 , .0104167 , .00520833 , .00130208] ,
		  [6 , 29.5735 , 2 , .0295735 , .000029574 , .0625 , .03125 , .0078125] ,
		  [202884 , 1000000 , 67628 , 1000 , 33814 , 2113.38 , 1056.69 , 264.172] ,
		  [96 , 473.176 , 32 , .473176 , 16 , .000473176 , .5 , .125] ,
		  [192 ,  946.353 , 64 , .946353 , 32 , .000946353 , 2 , .25] ,
		  [768 , 3785.41 , 256 , 3.78541 , 128 , .00378541 , 8 , 4] ,	
		 ]

temp_conv = [[.55555555 , (-1 * 32) , .55555555 , 459.67 , 1 , 459.67 , (-1 * .83333333) , 212 , .18333333 , (-1 * 32) ] ,
			 [1.8 , 32 , 1 , 273.15 , 1.8 , 273.15 , (-1 * 1.5) , 100 , 1 , .33] ,
			 [1.8 , (-1 * 459.67) , 1 , (-1 * 273.15) , 1.8 , 0 , (-1 * 1.5) , 373.15 , (-1 * .33) , 373.15] ,
			 [1 , (-1 * 459.67) , (-1 * .5555555) , 491.67 , .5555555 , 0 , (-1 * .83333333) , 671.67 , .18333333 , (-1 * 491.67)] ,
			 [(-1 * 1.2) , 212 , (-1 * .66666666) , 100 , (-1 * .6666666) , 373.15 , (-1 * 1.2) , 671.67 , (-1 * .22) , 33] ,
			 [5.45454545 , 32 , 3.03030303 , 0 , 3.03030303 , 273.15 , 5.45454545 , 491.67 , (-1 * .22) , 33] 
			]


n = 0
print "Unit Conversions"
print "What set?"
while n < 5:
	print (n + 1) , categories[n]
	n += 1
wc = raw_input("->")
wc = int(wc)
os.system('cls')
print "Starting unit?"
if wc == 1:
	c = 0
	print categories[0]
	while c < len(len_units):
		print (c + 1) , len_units[c]
		c += 1
	wu = raw_input("->")
	wu = int(wu)
	np = 1
	n = 0
	while np <= (len(len_units) - 1):
		if (n + 1) == wu:
			n += 1
		if (n + 1) != wu:
			print np , len_units[n]
			np += 1
			n += 1
	to = raw_input("->")
	to = int(to)
	print " "
	starting = raw_input("Amount ->")
	result = 0
	result = float(result)
	result = (float(starting)) * float(len_to[wu - 1][to - 1])
	print result
	os.system('pause')
	os.system('cls')
if wc == 2:
	c = 0 
	print categories[1]
	while c < len(mass_units):
		print (c + 1) , mass_units[c]
		c += 1
	wu = raw_input("->")
	wu = int(wu)
	np = 1
	n = 0
	while np <= (len(mass_units) - 1):
		if (n + 1) == wu:
			n += 1
		if (n + 1) != wu:
			print np , mass_units[n]
			np += 1
			n += 1
	to = raw_input("->")
	to = int(to)
	print " "
	starting = raw_input("Amount ->")
	result = 0
	result = float(result)
	result = (float(starting)) * float(mass_to[wu - 1][to - 1])
	print result
	os.system('pause')
	os.system('cls')
if wc == 3: 
	c = 0
	print categories[2]
	while c < len(vol_units):
		print (c + 1) , vol_units[c]
		c += 1
	wu = raw_input("->")
	wu = int(wu)
	np = 1
	n = 0
	while np <= (len(vol_units) - 1):
		if (n + 1) == wu:
			n += 1
		if (n + 1) != wu:
			print np , vol_units[n]
			np += 1
			n += 1
	to = raw_input("->")
	to = int(to)
	print " "
	starting = raw_input("Amount ->")
	result = 0
	result = float(result)
	result = (float(starting)) * float(vol_to[wu - 1][to - 1])
	print result
	os.system('pause')
	os.system('cls')
if wc == 4:
	c = 0
	print categories[3]
	while c < len(tem_units):
		print (c + 1) , tem_units[c]
		c += 1
	wu = raw_input("->")
	wu = int(wu)
	np = 1
	n = 0
	while np <= (len(tem_units) - 1):
		if (n + 1) == wu:
			n += 1
		if (n + 1) != wu:
			print np , tem_units[n]
			np += 1
			n += 1
	to = raw_input("->")
	to = int(to)
	print " "
	ta = (2 * (to - 1))
	print ta
	starting = raw_input("Amount ->")
	result = 0
	result = float(result)
	starting = float(starting)
	result = starting * temp_conv[wu -1][ta] + temp_conv[wu - 1][ta + 1]
	print result
	os.system('pause')
	os.system('cls')
if wc == 5:
	c = 0
	print categories[4]
	while c < len(currencies):
		print (c + 1) , currencies[c]
		c += 1
	wu = raw_input("->")
	wu = int(wu)
	np = 1
	n = 0
	while np <= (len(currencies) - 1):
		if (n + 1) == wu:
			n += 1
		if (n + 1) != wu:
			print np , currencies[n]
			np += 1
			n += 1

