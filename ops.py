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
	 	  "Side 2 =" , "Side 3 =" , "Base =" , "Power ="
	 	  "Height =" , "Radius =" , "Number of Sides =" , 
	 	  "Length of Sides =" , "Central Angle =" ] # 15


op_outs = ["Sum =" , "Difference =" , "Product =" , 
		   "Quotient =" , "Result =" , "Area =" , 
		   "Perimeter =" , "Circumference =" , 
		   "Arc Length =" , "Segment Area ="] # 10

log_outs = ["Form:Add = " , "Form:Sub = " , "Form:Mult = ", 
			"Form:Div = " , "Form:Exp = " , "Form:A_Tri = " ,
			"Form:P_Tri = " , "Form:S_Area = " , "Form:S_Perim = " , 
			"Form:R_Area = " , "Form:R_Perim = " , "Form:C_Area = " ,
			"Form:C_Circ = " , "Form:A_N-Gon = " , "Form:P_N-Gon = " ,
			"Form:A_Length = " , "Form:S_Area = " ] # 17

units = ["meters" , "kilometers" , "feet" , "yards" , "miles" , "milligrams" , 
		 "grams" , "kilograms" , "metric tons" , "ounces" , "pounds" , "tons" ,
		 "troy ounces" , "fl ounces" , "pints" , "quarts" , "gallons" , 
		 "farenheit" , "celsius" , "kelvin" , "rankine" , "delisle" , 
		 "Newton" , "USD" , "EUR" , "GBP" , "CAD" , "JPY", "CNY"]

len_factors = [.001 , 3.28084 , 1.09361 , .000621371 , 1000 , 3280.84 , 
			   1093.61 , .621371 , .3048 , .0003048 , .33333333 , 
			   .000189394 , .9144 , .0009144 , 3 , .000568182 , 
			   1609.34 , 1.60934 , 5280 , 1760 ]

# 0 m to k    # 4 k to m   #  8 f to m   # 12 y to m   # 16 mi to m
# 1 m to f    # 5 k to f   #  9 f to k   # 13 y to k   # 17 mi to k
# 2 m to y    # 6 k to y   # 10 f to y   # 14 y to f   # 18 mi to f
# 3 m to mi   # 7 k to mi  # 11 f to mi  # 15 y to mi  # 19 mi to y


mass_factors = []