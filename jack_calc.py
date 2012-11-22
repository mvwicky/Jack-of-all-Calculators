# MATRIX MATH PORT TO PYTHON

import math
import os
import time

Pi = 3.141592
DEG_TO_RAD = (Pi / 180)
a = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
c = [1 , 2 , 4 , 4 , 5 , 6 , 7 , 8 , 9]
ops = ["Addition" , "Subtraction" , "Multiplication" , 
	   "Division" , "Exponentation" , 
	   "Area of a Triangle" , "Perimeter of a Triangle" , 
	   "Area of a Square" , "Perimeter of a Square" , 
	   "Area of a Rectangle" , "Perimeter of a Rectangle" , 
	   "Area of a Circle" , "Circumference of a Circle" , 
	   "Area of an N-Gon" , "Perimeter of an N-Gon" , 
	   "Arc Length" , "Area of a Segment of a Circle" , 
	   "Unit Conversions"]

op_ins = ["Number 1 =" , "Number 2 =" , "Dividend =" , 
	 	  "Divisor =" , "Side =" , "Side 1 =" , 
	 	  "Side 2 =" , "Side 3 =" , "Base =" , "Power =" ,
	 	  "Height =" , "Radius =" , "Number of Sides =" , 
	 	  "Length of Sides =" , "Central Angle =" ] # 14

op_outs = ["Sum =" , "Difference =" , "Product =" , 
		   "Quotient =" , "Result =" , "Area =" , 
		   "Perimeter =" , "Circumference =" , 
		   "Arc Length =" , "Segment Area ="] # 10

log_outs = ["Form:Add = " , "Form:Sub = " , "Form:Mult = ", 
			"Form:Div = " , "Form:Exp = " , "Form:P_Tri = " ,
			"Form:A_Tri = " , "Form:S_Area = " , "Form:S_Perim = " , 
			"Form:R_Area = " , "Form:R_Perim = " , "Form:C_Area = " ,
			"Form:C_Circ = " , "Form:A_N-Gon = " , "Form:P_N-Gon = " ,
			"Form:A_Length = " , "Form:S_Area = " ] # 17

units = ["meters" , "kilometers" , "feet" , "yards" , "miles" , "milligrams" , 
		 "grams" , "kilograms" , "metric tons" , "ounces" , "pounds" , "tons" ,
		 "troy ounces" , "fl ounces" , "pints" , "quarts" , "gallons" , 
		 "farenheit" , "celsius" , "kelvin" , "rankine" , "delisle" , 
		 "Newton" , "USD" , "EUR" , "GBP" , "CAD" , "JPY", "CNY"]

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


waiting = ["W" , "a" , "i" , "t" , "i" , "n" , "g" , "." , "." , "."]

start_time = time.time()
log = open("log.txt" , "a")

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
		print " "
		print "Done" 

def conv_log(t , f , s , r):
	log.write(str(s))
	log.write(" ")
	log.write(units[t])
	log.write(" converted to ")
	log.write(str(r))
	log.write(" ")
	log.write(units[f])
	log.write("\n")
	log.flush()

def log_write(out , n):
	log.write(log_outs[n])
	log.write(str(out))
	log.write("\n")
	log.flush()

def show_functions(o):
	n = 1
	while n <= o:
		print n , ops[n]
		n += 1

def board(a):
	print "| " , a[0] , " | " , a[1] , " | " , a[2] , " |"
	print "| " , a[3] , " | " , a[4] , " | " , a[5] , " |"
	print "| " , a[6] , " | " , a[7] , " | " , a[8] , " |"
	
def spa():
	print ""

def initialize_matrix(a):
	n = 0
	while n <= 8:
		a[n] = 0
		n += 1
	return a

def assign_values(a , s , v):
	a[s] = v
	
def assign_all_values(a , v):
	n = 0
	while n <= 8:
		a[n] = v
		n += 1
	return a

def addition(x , y):
	sum = x + y
	log_write(sum , 0)
	return sum
	
def subtraction(x , y):
	difference = x + y
	log_write(difference , 1)
	return difference

def multiplication(x , y):
	product = x * y
	log_write(product , 2)
	return product
	
def division(x , y):
	quotient = float(x) / float(y)
	log_write(quotient , 3)
	return quotient

def exponentation(x , y):
	result = math.pow(x , y)
	log_write(result , 4)
	return result
	
def area_tri(B , H):
	area = (B * H) / 2
	log_write(area , 5)
	return area
	
def perim_tri(s1 , s2 , s3):
	valid_triangle = 0
	if s1 + s2 < s3:
		valid_triangle = 0
	if s2 + s3 < s1:
		valid_triangle = 0
	if s1 + s3 < s2:
		valid_triangle = 0
	if s1 + s2 > s3 & s2 + s3 > s1 & s1 + s3 > s2:
		valid_triangle = 1
	if valid_triangle == 1:
		perim = s2 + s2 + s3
		log_write(perim , 6)
		log.flush()
		return perim
	if valid_triangle == 0:
		log_write(-1 , 6)
		return -1
		
def area_square(s):
	area = s * s
	log_write(area , 7)
	return area

def perim_square(s):
	perim = s * 4
	log_write(perim , 8)
	return perim

def area_rectangle(s1, s2):
	area = s1 * s2
	log_write(area , 9)
	return area

def perim_rectangle(s1 , s2):
	perim = (2 * s1) + (2 * s2)
	log_write(perim , 10)
	return perim
	
def area_circle(r):
	area = Pi * (r * r)
	log_write(area , 11)
	return area
	
def circumference(r):
	cir = (2 * r) * Pi
	log_write(cir , 12)
	return cir

def area_ngon(n , l):
	area = (.25 * (n * (l * l)) * (1 / math.tan(Pi / n)))
	log_write(area , 13)
	return area

def perim_ngon(n , l):
	perim = n * l
	log_write(perim , 14)
	return perim

def arc_length(t , r):
	l = t * r
	log_write(l , 15)
	return l

def segment_area(t , r):
	a = ((r**2) / 2 ) * ( (DEG_TO_RAD * t) - math.sin(DEG_TO_RAD * t) ) 
	log_write(a , 16)
	return a

def adding_columns(a , c):
	if c == 1:
		sum = a[0] + a[3] + a[6]
	if c == 2:
		sum = a[1] + a[4] + a[7]
	if c == 3:
		sum = a[2] + a[5] + a[8]
	return sum
	
def sub_columns(a , c):
	if c == 1:
		diff = a[0] - a[3] - a[6]
	if c == 2:
		diff = a[1] - a[4] - a[7]
	if c == 3:
		diff = a[2] - a[5] - a[8]
	return diff

def mult_columns(a , c):
	if c == 1:
		prod = a[0] * a[3] * a[6]
	if c == 2:
		prod = a[1] * a[4] * a[7]
	if c == 3:
		prod = a[2] * a[5] * a[8]
	return prod
	
def div_columns(a , c):
	if c == 1:
		quot = a[0] / a[3] / a[6]
	if c == 2:
		quot = a[1] / a[4] / a[7]
	if c == 3:
		quot = a[2] / a[5] / a[8]
	return quot
	
def adding_rows(a , r):
	if r == 1:
		sum = a[0] + a[1] + a[2]
	if r == 2:
		sum = a[3] + a[4] + a[5]
	if r == 3:
		sum = a[6] + a[7] + a[8]
	return sum
	
def sub_rows(a , r):
	if r == 1:
		diff = a[0] - a[1] - a[2]
	if r == 2:
		diff = a[3] - a[4] - a[5]
	if r == 3:
		diff = a[6] - a[7] - a[8]
	return diff
	
def mult_rows(a , r):
	if r == 1:
		prod = a[0] * a[1] * a[2]
	if r == 2:
		prod = a[3] * a[4] * a[5]
	if r == 3:
		prod = a[6] * a[7] * a[8]
	return prod

def div_rows(a , r):
	if r == 1:
		quot = a[0] / a[1] / a[2]
	if r == 2:
		quot = a[3] / a[4] / a[5]
	if r == 3:
		quot = a[6] / a[7] / a[8]
	return quot

def adding_diag(a , d):
	if d == 1:
		sum = a[0] + a[4] + a[8]
	if d == 2:
		sum = a[2] + a[4] + a[6]
	return sum

def sub_diag(a , d):
	if d == 1: 
		diff = a[0] - a[4] - a[8]
	if d == 2:
		diff = a[2] - a[4] - a[6]
	return diff

def mult_diag(a , d):
	if d == 1:
		prod = a[0] * a[4] * a[8]
	if d == 2:
		prod = a[2] * a[4] * a[6]
	return prod

def div_diag(a , d):
	if d == 1:
		quot = a[0] / a[4] / a[8]
	if d == 2:
		quot = a[2] / a[4] / a[6]
	return quot
	
def unit_conversions():
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


def do_things():
	stay_d = 1
	while stay_d == 1:
		print "1. Columns"
		print "2. Rows"
		print "3. Diagonals"
		print "4. Formulas"
		print "5. Unit Conversions"
		print "6. Matrix Editing"
		print "7. Alarm"
		c = input()
		os.system('cls')
		stay_c = 1
		if c == 1: # Columns
			while stay_c == 1:
				show_functions(4)
				ic = input()
				spa()
				if ic == 1: # Adding Columns
					print "Column = "
					f = input()
					print adding_columns(a , f)
					log_sum = adding_columns(a , f)
					log.write("Column:Add =  ")
					log.write(str(log_sum))
					log.write("\n")
					os.system('pause')
				if ic == 2: # Subtracting Columns
					print "Column = "
					f = input()
					print sub_columns(a , f)
					log_diff = sub_columns(a , f)
					log.write("Column:Sub =  ")
					log.write(str(log_diff))
					log.write("\n")
					os.system('pause')
				if ic == 3: # Multiplying Columns
					print "Column = "
					f = input()
					print mult_columns(a , f)
					log_prod = mult_columns(a , f)
					log.write("Column:Mult =  ")
					log.write(str(log_prod))
					log.write("\n")
					os.system('pause')
				if ic == 4: # Dividing Columns
					print "Column = "
					f = input()
					print div_columns(a , f)
					log_quot = div_columns(a , f)
					log.write("Column:Div =  ")
					log.write(str(log_quot))
					log.write("\n")
					os.system('pause')
				os.system('cls')
				print "Stay in Columns?"
				stay_c = input()
				os.system('cls')
		stay_r = 1
		if c == 2: # Rows
			while stay_r == 1:
				show_functions(4)
				r = input()
				spa()
				if r == 1: # Adding Rows
					print "Row = "
					f = input()
					print adding_rows(a , f)
					log_sum = adding_rows(a , f)
					log.write("Row:Add =  ")
					log.write(str(log_sum))
					log.write("\n")
					os.system('pause')
				if r == 2: # Subtracting Rows
					print "Row = "
					f = input()
					print sub_rows(a , f)
					log_diff = sub_rows(a , f)
					log.write("Row:Sub =  ")
					log.write(str(log_diff))
					log.write("\n")
					os.system('pause')
				if r == 3: # Multiplying Rows
					print "Row ="
					f = input()
					print mult_rows(a , f)
					log_prod = mult_rows(a , f)
					log.write("Row:Mult =  ")
					log.write(str(log_prod))
					log.write("\n")
					os.system('pause')
				if r == 4: # Dividing Rows
					print "Row = "
					f = input()
					print div_rows(a , f)
					log_quot = div_rows(a , f)
					log.write("Row:Div =  ")
					log.write(str(log_quot))
					log.write("\n")
					os.system('pause')
				os.system('cls')
				print "Stay in Rows?"
				stay_r = input()
				os.system('cls')
		stay_d = 1
		if c == 3: # Diagonals
			while stay_d == 1:
				show_functions(4)
				d = input()
				spa()
				if d == 1: # Adding Diagonals
					print "Diagonal = "
					f = input()
					print adding_diag(a , f)
					log_sum = adding_diag(a , f)
					log.write("Diag:Add =  ")
					log.write(str(log_sum))
					log.write("\n")
					os.system('pause')
				if d == 2: # Subtracting Diagonals
					print "Diagonal = "
					f = input()
					print sub_diag(a , f)
					log_diff = sub_diag(a , f)
					log.write("Diag:Sub =  ")
					log.write(str(log_diff))
					log.write("\n")
					os.system('pause')
				if d == 3: # Multiplying Diagonals
					print "Diagonal = "
					f = input()
					print mult_diag(a , f)
					log_prod = mult_diag(a , f)
					log.write("Diag:Mult =  ")
					log.write(str(log_prod))
					log.write("\n")
					os.system('pause')
				if d == 4: # Dividing Diagonals
					print "Diagonal = "
					f = input()
					print div_diag(a , f)
					log_quot = div_diag(a , f)
					log.write("Diag:Div =  ")
					log.write(str(log_quot))
					log.write("\n")
					os.system('pause')
				os.system('cls')
				print "Stay in Diagonals?"
				stay_d = input()
				os.system('cls')
		stay_f = 1
		if c == 4: # Formulas
			while stay_f == 1:
				n = 1
				num_ops = 17
				while n <= num_ops:
					print n, ops[n-1]
					n += 1  
				f = input()
				os.system('cls')
				if f == 1: # Addition
					print ops[0]
					print op_ins[0]
					s1 = input()
					print op_ins[1]
					s2 = input()
					print op_outs[0] , addition(s1, s2)
					os.system('pause')
				if f == 2: # Subtraction
					print op_ins[0]
					s1 = input()
					print op_ins[1]
					s2 = input()
					print op_outs[1] , subtraction(s1 , s2)
					os.system('pause')
				if f == 3: # Multiplication
					print op_ins[0]
					s1 = input()
					print op_ins[1]
					s2 = input()
					print op_outs[2] , multiplication(s1 , s2)
					os.system('pause')
				if f == 4: # Division
					print op_ins[2]
					s1 = input()
					print op_ins[3]
					s2 = input()
					print op_outs[3] , division(s1 , s2)
					os.system('pause')
				if f == 5: # Exponentation
					print op_ins[8]
					s1 = input()
					print op_ins[9]
					s2 = input()
					print op_outs[4] , exponentation(s1 , s2)
					os.system('pause')
				if f == 6: # Area Triangle
					print op_ins[8]
					s1 = input()
					print op_ins[10]
					s2 = input()
					print op_outs[5] , area_tri(s1 , s2)
					os.system('pause')
				if f == 7: # Perim Triangle
					print op_ins[5]
					s1 = input()
					print op_ins[6]
					s2 = input()
					print op_ins[7]
					s3 = input()
					print op_outs[6] , perim_tri(s1 , s2 , s3)
					os.system('pause')
				if f == 8: # Area Square
					print op_ins[4]
					s1 = input()
					print op_outs[5] , area_square(s1)
					os.system('pause')
				if f == 9: # Perim Square
					print op_ins[4]
					s1 = input()
					print op_outs[6] , perim_square(s1)
					os.system('pause')
				if f == 10: # Area Rectangle
					print op_ins[5]
					s1 = input()
					print op_ins[6]
					s2 = input()
					print op_outs[5] , area_rectangle(s1 , s2)
					os.system('pause')
				if f == 11: # Perim Recatangle
					print op_ins[5]
					s1 = input()
					print op_ins[6]
					s2 = input()
					print op_outs[6] , perim_rectangle(s1 , s2)
					os.system('pause')
				if f == 12: # Area Circle
					print op_ins[11]
					s1 = input()
					print op_outs[5] , area_circle(s1)
					os.system('pause')
				if f == 13: # Circumference Circle
					print op_ins[11]
					s1 = input()
					print op_outs[7] , circumference(s1)
					os.system('pause')
				if f == 14: # Area N-Gon
					print op_ins[12]
					s1 = input()
					print op_ins[13]
					s2 = input()
					print op_outs[5] , area_ngon(s1 , s2)
					os.system('pause')
				if f == 15: # Perim N-Gon 
					print op_ins[12]
					s1 = input()
					print op_ins[13]
					s2 = input()
					print op_outs[6] , perim_ngon(s1 , s2)
					os.system('pause')
				if f == 16: # Arc Length
					print op_ins[14]
					t = input()
					print op_ins[11]
					r = input()
					print op_outs[8] , arc_length(t , r)
					os.system('pause')
				if f == 17: # Segment Circle
					print op_ins[14]
					t = input()
					print op_ins[11]
					r = input()
					print op_outs[9] , segment_area(t , r)
					os.system('pause')
				os.system('cls')
				print "Stay in Formulas?"
				stay_f = input()
				os.system('cls')
		os.system('cls')
		stay_e = 1
		if c == 5:
			unit_conversions()
		if c == 6: # Matrix Editing
			while stay_e == 1:
				print "1. Initialize Matrix to 0"
				print "2. Assign one value to all spots"
				print "3. Assign a value to one spot"
				e = input()
				os.system('cls')
				if e == 1: # initialize matrix
					print ""
					initialize_matrix(a)
					board(a)
					os.system('pause')
					log.write("Matrix Initialized")
					log.write("\n")
				if e == 2: # assign all values
					os.system('cls')
					print "Value = "
					v = input()
					assign_all_values(a , v)
					board(a)
					os.system('pause')
					log.write("All spots set to ")
					log.write(str(v))
					log.write("\n")
				if e == 3: # assign value
					os.system('cls')
					print "Spot = "
					s = input()
					print "Value = "
					v = input()
					assign_values(a , s , v)
					board(a)
					os.system('pause')
					log.write("Spot ")
					log.write(str(s))
					log.write(" set to ")
					log.write(str(v))
					log.write("\n")
				os.system('cls')
				print "Stay in Matrix Edit Mode?"
				stay_e = input()
				os.system('cls')
		if c == 7:
			print "Alarm"
			when = raw_input("How many minutes? ->")
			alarm(when)
		print "Stay on?"
		stay_d = input()
		os.system('cls')

do_things()