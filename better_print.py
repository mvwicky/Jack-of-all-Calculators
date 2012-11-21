import os

categories = ["Length" , "Mass/Weight" , "Volume" , "Temperature" , "Currency"]

len_units = ["Meters" , "Millimeters" , "Feet" , "Yards" , "Miles"]

mass_units = ["Milligrams" ,  "Grams" , "Kilograms" , "Metric tons" , "Ounces" , 
			  "Pounds" , "Tons" , "Troy Ounces"]

vol_units = ["Teaspoon" , "Milliliter" , "Tablespoon" , "Liter" , "Ounce" , 
	    	 "Cubic Meter" , "Pint" , "Quart" , "Gallon"]

tem_units = ["Farenheit" , "Celsius" , "Kelvin" , "Rankine" , "Delisle"]

currencies = ["USD" , "EUR" , "GBP" , "CAD" , "JPY", "CNY"]

len_factors = [.001 , 3.28084 , 1.09361 , .000621371 , 
		       1000 , 3280.84 , 1093.61 , .621371 , 
		      .3048 , .0003048 , .33333333 , .000189394 , 
		      .9144 , .0009144 , 3 , .000568182 , 
		    1609.34 , 1.60934 , 5280 , 1760 ]

# 0 m to k    # 4 k to m   #  8 f to m   # 12 y to m   # 16 mi to m
# 1 m to f    # 5 k to f   #  9 f to k   # 13 y to k   # 17 mi to k
# 2 m to y    # 6 k to y   # 10 f to y   # 14 y to f   # 18 mi to f
# 3 m to mi   # 7 k to mi  # 11 f to mi  # 15 y to mi  # 19 mi to y


n = 0
print "Unit Conversions"
print "What set?"
while n < 5:
	print (n + 1) , categories[n]
	n += 1
wc = raw_input("->")
wc = int(wc)
os.system('cls')
if wc == 1:
	c = 0
	print categories[0]
	while c < len(len_units):
		print (c + 1) , len_units[c]
		c += 1
	wu = raw_input("->")
	wu = int(wu)
	np = 1
	while wu < len(len_units): 
		if wu == (len(len_units) - wu):
			wu += 1
		elif wu != (len(len_units) - wu):
			print np , len_units[wu]
			wu += 1
			np += 1
if wc == 2:
	c = 0 
	print categories[1]
	while c < len(mass_units):
		print (c + 1) , mass_units[c]
		c += 1
if wc == 3: 
	c = 0
	print categories[2]
	while c < len(vol_units):
		print (c + 1) , vol_units[c]
		c += 1
if wc == 4:
	c = 0
	print categories[3]
	while c < len(tem_units):
		print (c + 1) , tem_units[c]
		c += 1
if wc == 5:
	c = 0
	print categories[4]
	while c < len(currencies):
		print (c + 1) , currencies[c]
		c += 1

