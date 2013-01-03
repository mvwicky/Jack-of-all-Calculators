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

#LENGTH FACTORS
len_factors = [.001 , 3.28084 , 1.09361 , .000621371 , 
		       1000 , 3280.84 , 1093.61 , .621371 , 
		      .3048 , .0003048 , .33333333 , .000189394 , 
		      .9144 , .0009144 , 3 , .000568182 , 
		    1609.34 , 1.60934 , 5280 , 1760 ]

#MASS FACTORS
mass_to = [[ .001 , .00001 , .00000001 , .000035274 , .0000022046 , .0000000011023 , .000321507466 ] ,
		   [1000 , .001 , .000001 , .035274 , .00220463 , .0000011023 , .0321507466 ] ,
		   [100000 , 1000 , .001 , 35.274 , 2.20462 , .00110231 , 32.1507466 ] ,
		   [1000000000 , 100000 , 1000 , 35274 , 2204.62 , 1.10231 , 32150.7466] ,
		   [28349.5 , 28.3495 , .0283495 , .00002835 , .0625 , .00003125 , .911458333] ,
		   [453492 , 453.592 , .453592 , .000453592 , 16 , .0005 , 14.5833333 ] ,
		   [907200000 , 907185 , 907.185 , .907185 , 32000 , 2000 , 29166.6667 ] ,
		   [31103.4768 , 31.1034768 , .0311034768 , .0000311034768 , 1.09714286 , .0685714286 , .0000342857143]
			]

#VOLUME FACTORS

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

#TEMPERATURE FACTORS

temp_conv = [
			 [.55555555 , -32 , .55555555 , 459.67 , 1 , 459.67 , -.83333333 , 212 , .18333333 , -32 ]
			 [1.32 , -8 , 1 , 273.15 , 1.8 , 273.15 , -1.5 , 100 , 1 , .33]
			 [1.8 , -459.67 , 1 , -273.15 , 1.8 , 0 , -1.5 , 373.15 , -.33 , 373.15]
			 [1 , -459.67 , -.5555555 , 491.67 , .5555555 , 0 , -.83333333 , 671.67 , .18333333 , -491.67]
			 [-1.2 , 212 , -.66666666 , 100 , -.6666666 , 373.15 , -1.2 , 671.67 , -.22 , 33]
			 [5.45454545 , 32 , 3.03030303 , 0 , 3.03030303 , 273.15 , 5.45454545 , 491.67 , -.22 , 33]
			]

#CURRENCY FACTORS

