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

len_factors = []

start_time = time.time()
log = open("log.txt" , "a")


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
	print "1. Length"
	print "2. Mass/Weight"
	print "3. Volume"
	print "4. Temperature"
	print "5. Currency"
	i = input()
	if i == 1: # Length
		print "Starting Unit"
		print "1. Meter       3. Foot"
		print "2. Kilometer   4. Yard"
		print "               5. Mile"
		q = input()
		if q == 1: # meters to
			print "Meters to"
			print "1. Kilometer"
			print "2. Foot"
			print "3. Yard"
			print "4. Mile"
			h = input()
			if h == 1: # kilometers
				print "Meters = "
				a = input()
				r = float(a) * .001
				print "In kilometers = " , r
				os.system('pause')
				conv_log(0 , 1 , a , r)
			if h == 2: # feet
				print "Meters = "
				a = input()
				r = float(a) * 3.28084
				print "In feet = " , r
				os.system('pause')
				conv_log(0 , 2 , a , r)
			if h == 3: # yards
				print "Meters = "
				a = input()
				r = float(a) * 1.09361
				print "In yards = " , r
				os.system('pause')
				conv_log(0 , 3 , a , r)
			if h == 4: # miles
				print "Meters = "
				a = input()
				r = float(a) * .000621371
				print "In miles = " , r	
				os.system('pause')
				conv_log(0 , 4 , a , r)	
		if q == 2: # kilometers to
			print "Kilometers to"
			print "1. Meter"
			print "2. Foot"
			print "3. Yard"
			print "4. Mile"
			h = input()
			if h == 1: # meters
				print "Kilometers = "
				a = input()
				r = float(a) * 1000
				print "In meters = " , r
				os.system('pause')
				conv_log(1 , 0 , a , r)
			if h == 2: # feet
				print "Kilometers = "
				a = input()
				r = float(a) * 3280.84
				print "In feet = " , r
				os.system('pause')
				conv_log(1 , 2 , a , r)
			if h == 3: # yards
				print "Kilometers = "
				a = input()
				r = float(a) * 1093.61
				print "In yards = " , r
				os.system('pause')
				conv_log(1 , 3 , a , r)
			if h == 4: # miles
				print "Kilometers = "
				a = input()
				r = float(a) * .621371	
				print "In miles = " , r
				os.system('pause')
				conv_log(1 , 4 , a , r)	
		if q == 3: # feet to
			print "Feet to"
			print "1. Meter"
			print "2. Kilometer"
			print "3. Yard"
			print "4. Mile"
			h = input()
			if h == 1: # meters
				print "Feet = "
				a = input()
				r = float(a) * .3048
				print "In meters = " , r
				os.system('pause')
				conv_log(2 , 0 , a , r)
			if h == 2: # kilometers
				print "Feet = "
				a = input()
				r = float(a) * .0003048
				print "In kilometers = " , r
				os.system('pause')
				conv_log(2 , 1 , a , r)
			if h == 3: # yards
				print "Feet = "
				a = input()
				r = float(a) * .33333333
				print "In yards = " , r
				os.system('pause')
				conv_log(2 , 3 , a , r)
			if h == 4: # miles
				print "Feet = "
				a = input()
				r = float(a) * .000189394
				print "In miles = " , r
				os.system('pause')
				conv_log(2 , 4 , a , r)	
		if q == 4: # yards to
			print "Yards to"
			print "1. Meter"
			print "2. Kilometer"
			print "3. Foot"
			print "4. Mile"
			h = input()
			if h == 1: # meters
				print "Yards = "
				a = input()
				r = float(a) * .9144
				print "In meters = " , r
				os.system('pause')
				conv_log(3 , 0 , a , r)
			if h == 2: # kilometers
				print "Yards = "
				a = input()
				r = float(a) * .0009144
				print "In kilometers = " , r
				os.system('pause')
				conv_log(3 , 1 , a , r)
			if h == 3: # feet
				print "Yards = "
				a = input()
				r = float(a) * 3
				print "In feet = " , r
				os.system('pause')
				conv_log(3 , 2 , a , r)
			if h == 4: # mile
				print "Yards = "	
				a = input()
				r = float(a) * .000568182
				print "In miles = " , r
				os.system('pause')
				conv_log(3 , 4 , a , r)	
		if q == 5: # miles to
			print "Miles to"
			print "1. Meter"
			print "2. Kilometer"
			print "3. Foot"
			print "4. Yard"
			if h == 1: # meters
				print "Miles = "
				a = input()
				r = float(a) * 1609.34
				print "In meters = " , r
				os.system('pause')
				conv_log(4 , 0 , a , r)
			if h == 2: # kilometers
				print "Miles = "
				a = input()
				r = float(a) * 1.60934
				print "In kilometers = " , r
				os.system('pause')
				conv_log(4 , 1 , a , r)
			if h == 3: # feet
				print "Miles = "
				a = input()
				r = float(a) * 5280
				print "In feet = " , r
				os.system('pause')
				conv_log(4 , 2 , a , r)
			if h == 4: # yards
				print "Miles = "
				a = input() 
				r = float(a) * 1760
				print "In yards = " , r
				os.system('pause')	
				conv_log(4 , 3 , a , r)
			os.system('pause')
	if i == 2: # Mass/Weight
		print "Starting Unit"
		print "1. Milligram   5. Ounce"
		print "2. Gram        6. Pound"
		print "3. Kilogram    7. Ton"
		print "4. Metric Ton  8. Troy Ounce"
		q = input()
		if q == 1:
			print "Milligrams to"
			print "1. Grams"
			print "2. Kilograms"
			print "3. Metric Tons"
			print "4. Ounces"
			print "5. Pounds"
			print "6. Tons"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Milligrams = "
				a = input()
				r = float(a) * .001
				print "In grams = " , r
				os.system('pause')
				conv_log(5 , 6 , a , r)
			if h == 2:
				print "Milligrams = "
				a = input()
				r = float(a) * .000001
				print "In kilograms = " , r
				os.system('pause')
				conv_log(5 , 7 , a , r)
			if h == 3:
				print "Milligrams = "
				a = input()
				r = float(a) * .000000001
				print "In metric tons = " , r
				os.system('pause')
				conv_log(5 , 8 , a , r)
			if h == 4:
				print "Milligrams = "
				a = input()
				r = float(a) * .000035274
				print "In ounces = " , r
				os.system('pause')
				conv_log(5 , 9 , a , r)
			if h == 5:
				print "Milligrams = "
				a = input()
				r = float(a) * .0000022046
				print "In pounds = " , r
				os.system('pause')
				conv_log(5 , 10 , a , r)
			if h == 6:
				print "Milligrams = "
				a = input()
				r = float(a) * .0000000011023
				print "In tons = " , r
				os.system('pause')
				conv_log(5 , 11 , a , r)
			if h == 7:
				print "Milligrams = "
				a = input()
				r = float(a) * .0000321507466
				print "In troy ounces = " , r
				os.system('pause')
				conv_log(5 , 11 , a , r)
		if q == 2:
			print "Grams to"
			print "1. Milligrams"
			print "2. Kilograms"
			print "3. Metric Tons"
			print "4. Ounces"
			print "5. Pounds"
			print "6. Tons"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Grams = "
				a = input()
				r = float(a) * 1000
				print "In milligrams = " , r
				os.system('pause')
				conv_log(6 , 5 , a , r)
			if h == 2:
				print "Grams = "
				a = input()
				r = float(a) * .001
				print "In kilograms = " , r
				os.system('pause')
				conv_log(6 , 7 , a , r)
			if h == 3:
				print "Grams = "
				a = input()
				r = float(a) * .000001
				print "In metric tons = " , r
				os.system('pause')
				conv_log(6 , 8 , a , r)
			if h == 4:
				print "Grams = "
				a = input()
				r = float(a) * .035274
				print "In ounces = " , r
				os.system('pause')
				conv_log(6 , 9 , a , r)
			if h == 5:
				print "Grams = "
				a = input()
				r = float(a) * .00220462
				print "In pounds = " , r
				os.system('pause')
				conv_log(6 , 10 , a , r)
			if h == 6:
				print "Grams = "
				a = input()
				r = float(a) * .0000011023
				print "In tons = " ,  r
				os.system('pause')
				conv_log(6 , 11 , a , r)
			if h == 7:
				print "Grams = "
				a = input()
				r = float(a) * .0321507466
				print "In troy ounces = " , r
				os.system('pause')
				conv_log(6 , 12 , a , r)
		if q == 3:
			print "Kilograms to"
			print "1. Milligrams"
			print "2. Grams"
			print "3. Metric Tons"
			print "4. Ounces"
			print "5. Pounds"
			print "6. Tons"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Kilograms = "
				a = input()
				r = float(a) * 1000000
				print "In milligrams = " , r
				os.system('pause')
			if h == 2:
				print "Kilograms = "
				a = input()
				r = float(a) * 1000
				print "In grams = " , r
				os.system('pause')
			if h == 3:
				print "Kilograms = "
				a = input()
				r = float(a) * .001
				print "In metric tons = " , r
				os.system('pause')
			if h == 4:
				print "Kilograms = "
				a = input()
				r = float(a) * 35.274
				print "In ounces = " , r
				os.system('pause')
			if h == 5:
				print "Kilograms = "
				a = input()
				r = float(a) * 2.20462
				print "In pounds = " , r
				os.system('pause')
			if h == 6:
				print "Kilograms = "
				a = input()
				r = float(a) * .00110231
				print "In tons = " , r
				os.system('pause')
			if h == 7:
				print "Kilograms = "
				a = input()
				r = float(a) * 32.1507466
				print "In troy ounces = " , r
				os.system('pause')
		if q == 4:
			print "Metric Tons to"
			print "1. Milligrams"
			print "2. Grams"
			print "3. Kilograms"
			print "4. Ounces"
			print "5. Pounds"
			print "6. Tons"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Metric Tons = "
				a = input()
				r = float(a) * 1000000000
				print "In milligrams = " , r
				os.system('pause')
			if h == 2:
				print "Metric Tons = "
				a = input()
				r = float(a) * 1000000
				print "In grams = " , r
				os.system('pause')
			if h == 3:
				print "Metric Tons = "
				a = input()
				r = float(a) * 1000
				print "In Kilograms = " , r
				os.system('pause') 
			if h == 4:
				print "Metric Tons = "
				a = input()
				r = float(a) * 35274
				print "In ounces = " , r
				os.system('pause')
			if h == 5:
				print "Metric Tons = "
				a = input()
				r = float(a) * 2204.62
				print "In pounds = " , r
				os.system('pause')
			if h == 6:
				print "Metric Tons = "
				a = input()
				r = float(a) * 1.10231
				print "In tons = " , r
				os.system('pause')
			if h == 7:
				print "Metric Tons = "
				a = input()
				r = float(a) * 32150.7466
				print "In troy ounces = " , r
				os.system('pause')
		if q == 5:
			print "Ounces to"
			print "1. Milligrams"
			print "2. Grams"
			print "3. Kilograms"
			print "4. Metric tons"
			print "5. Pounds"
			print "6. Tons"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Ounces = "
				a = input()
				r = float(a) * 28349.5
				print "In milligrams = " , r
				os.system('pause')
			if h == 2:
				print "Ounces = "
				a = input()
				r = float(a) * 28.3495
				print "In grams = " , r
				os.system('pause')
			if h == 3:
				print "Ounces = "
				a = input()
				r = float(a) * .0283495
				print "In kilograms = " , r
				os.system('pause')
			if h == 4:
				print "Ounces = "
				a = input()
				r = float(a) * .00002835
				print "In metric tons = " , r
				os.system('pause')
			if h == 5:
				print "Ounces = "
				a = input()
				r = float(a) * .0625
				print "In pounds = " , r
				os.system('pause')
			if h == 6:
				print "Ounces = "
				a = input()
				r = float(a) * .00003125
				print "In tons = " , r
				os.system('pause')
			if h == 7:
				print "Ounces = "
				a = input()
				r = float(a) * .911458333
				print "In troy ounces = " , r
				os.system('pause')
		if q == 6:
			print "Pounds to"
			print "1. Milligrams"
			print "2. Grams"
			print "3. Kilograms"
			print "4. Metric tons"
			print "5. Ounces"
			print "6. Tons"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Pounds = "
				a = input()
				r = float(a) * 453592
				print "In milligrams = " , r
				os.system('pause')
			if h == 2:
				print "Pounds = "
				a = input()
				r = float(a) * 453.592
				print "In grams = " , r
				os.system('pause')
			if h == 3:
				print "Pounds = "
				a = input()
				r = float(a) * .453592
				print "In kilograms = " , r
				os.system('pause')
			if h == 4:
				print "Pounds = "
				a = input()
				r = float(a) * .000453592
				print "In metric tons = " , r
				os.system('pause')
			if h == 5:
				print "Pounds = "
				a = input()
				r = float(a) * 16
				print "In ounces = " , r
				os.system('pause')
			if h == 6:
				print "Pounds = "
				a = input()
				r = float(a) * .0005
				print "In tons = " , r
				os.system('pause')
			if h == 7:
				print "Pounds = "
				a = input()
				r = float(a) * 14.5833333
				print "In troy ounces = " , r
				os.system('pause')
		if q == 7:
			print "Tons to"
			print "1. Milligrams"
			print "2. Grams"
			print "3. Kilograms"
			print "4. Metric tons"
			print "5. Ounces"
			print "6. Pounds"
			print "7. Troy Ounces"
			h = input()
			if h == 1:
				print "Tons = "
				a = input()
				r = float(a) * 907200000
				print "In milligrams = " , r
				os.system('pause')
			if h == 2:
				print "Tons = "
				a = input()
				r = float(a) * 907185
				print "In grams = " , r
				os.system('pause')
			if h == 3:
				print "Tons = "
				a = input()
				r = float(a) * 907.185
				print "In kilograms = " , r
				os.system('pause')
			if h == 4:
				print "Tons = "
				a = input()
				r = float(a) * .907185
				print "In metric tons = " , r
				os.system('pause')
			if h == 5:
				print "Tons = "
				a = input()
				r = float(a) * 32000
				print "In ounces = " , r
				os.system('pause')
			if h == 6:
				print "Tons = "
				a = input()
				r = float(a) * 2000
				print "In pounds = " , r
				os.system('pause')
			if h == 7:
				print "Tons = "
				a = input()
				r = float(a) * 29166.6667
				print "In troy ounces = " , r
				os.system('pause')
		if q == 8:
			print "Troy Ounces to"
			print "1. Milligrams"
			print "2. Grams"
			print "3. Kilograms"
			print "4. Metric tons"
			print "5. Ounces"
			print "6. Pounds"
			print "7. Tons"
			h = input()
			if h == 1:
				print "Troy Ounces = "
				a = input()
				r = float(a) * 31103.4768
				print "In milligrams = " , r
				os.system('pause')
			if h == 2:
				print "Troy Ounces = "
				a = input()
				r = float(a) * 31.1034768
				print "In grams = " , r
				os.system('pause')
			if h == 3:
				print "Troy Ounces = "
				a = input()
				r = float(a) * .0311034768
				print "In kilograms = " , r
				os.system('pause')
			if h == 4:
				print "Troy Ounces = "
				a = input()
				r = float(a) * .0000311034768
				print "In metric tons = " , r
				os.system('pause')
			if h == 5:
				print "Troy Ounces = "
				a = input()
				r = float(a) * 1.09714286
				print "In ounces = " , r
				os.system('pause')
			if h == 6:
				print "Troy Ounces = "
				a = input()
				r = float(a) * .0685714286
				print "In pounds = " , r
				os.system('pause')
			if h == 7:
				print "Troy Ounces = "
				a = input()
				r = float(a) * .0000342857143
				print "In tons = " , r
				os.system('pause')
	if i == 3: # Volume
		print "1. Teaspoon     7. Milliliter"
		print "2. Tablespoon   8. Liter"
		print "3. Ounce        9. Cubic Meter"
		print "4. Pint"
		print "5. Quart"
		print "6. Gallon"
		q = input()
	if i == 4: # Temperature
		print "1. Farenheit"
		print "2. Celsius"
		print "3. Kelvin"
		print "4. Rankine"
		print "5. Delisle"
		print "6. Newton"
		q = input()
	if i == 5: # Currency
		print "1. USD"
		print "2. EUR"
		print "3. GBP"
		print "4. CAD"
		print "5. JPY"
		print "6. CNY"
		q = input()

def do_things():
	stay_d = 1
	while stay_d == 1:
		print "1. Columns"
		print "2. Rows"
		print "3. Diagonals"
		print "4. Formulas"
		print "5. Matrix Editing"
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
				num_ops = 18
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
				if f == 18:
					print ""
					unit_conversions()
				os.system('cls')
				print "Stay in Formulas?"
				stay_f = input()
				os.system('cls')
		os.system('cls')
		stay_e = 1
		if c == 5: # Matrix Editing
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
		print "Stay on?"
		stay_d = input()
		os.system('cls')

do_things()