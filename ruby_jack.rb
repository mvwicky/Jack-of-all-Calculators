

pi = 3.141592
DEG_TO_RAG = (pi / 180)
a = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
ops = ["Addition" , "Subtraction" , "Multiplication" , 
	   "Division" , "Exponentation" , 
	   "Area of a Triangle" , "Perimeter of a Triangle" , 
	   "Area of a Square" , "Perimeter of a Square" , 
	   "Area of a Rectangle" , "Perimeter of a Rectangle" , 
	   "Area of a Circle" , "Circumference of a Circle" , 
	   "Area of an N-Gon" , "Perimeter of an N-Gon" , 
	   "Arc Length" , "Area of a Segment of a Circle" , 
	   ]

stay_d = 1
while stay_d == 1
	puts "1. Formulas"
	puts "2. Unit Conversions"
	c = gets.to_f
	if c == 1
		n = 0
		while n < 17
			print (n + 1), ". " , ops[n] 
			n += 1
			puts " "
		end
	end
	stay_d = gets.to_f 
end