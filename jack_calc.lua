-- JACK_CALC Lua
--[[
TODO-Make a function that takes in inputs to a table. 
	-Make a function that reads those inputs back into a operator function
	]]--
--base function definitions
function addition(...)
	local ag = select("#",...) -- number of args
	local n = 1
	local sum = 0
	while (n <= ag)
		do
		sum = sum + select(n,...)
		n = n + 1
	end
	print(sum) 
end

function subtraction(...)
	local ag = select("#",...) -- number of args
	local n = 1
	local diff = 0
	while (n <= ag)
		do
		diff = diff - select(n,...)
		n = n + 1
	end
	print(diff) 
end
 
function multiplication(...)
	local ag = select("#",...)-- number of args
	local n = 1
	local prod = 1
	while (n <= ag)
		do
		prod = prod * select(n,...)
		n = n + 1
	end
	print(prod)
end

function division(...)
	local ag = select("#",...) -- number of args
	local n = 1
	local quot = 1 
	while (n <= ag)
		do
		quot = quot / select(n,...)
		n = n + 1
	end
	print(quot)
end

function exponentation(b , p)
	local result
	result = math.pow(b , p)
	print(result)
end

function pick_one()
	io.write("1. Addition\n")
	io.write("2. Subtraction\n")
	io.write("3. Multiplication\n")
	io.write("4. Division\n")
	io.write("5. Exponentation\n")
	local wop = io.read()
	return wop
end

function do_stuff(dop)
	local in1
	local in2
	if dop == 1 then 
		addition(unpack(get_args()))
	end
	if dop == 2 then
		subtraction(unpack(get_args()))
	end
	if dop == 3 then
	io.write("Input 1 = ")
		multiplication(unpack(get_args()))
	end
	if dop == 4 then
		division(unpack(get_args()))
	end
	if dop == 5 then
		io.write("Base = ")
		in1 = io.read()
		io.write("\n")
		io.write("Power = ")
		in2 = io.read()
		io.write("\n")
		exponentation(in1 , in2)
	end
end

function get_args()
	local ags = {}
	local n = 1
	local ag
	while ag ~= "done"
		do
		io.write("Input ")
		io.write(n)
		io.write(": ")
		
		ag = assert(io.read("*number"), "invalid input")
		if ag == "done" or ag == " " or ag == "" then
			break
		end
		ag = tonumber(ag)
		ags[n] = ag
		n = n + 1
	end
	return ags
end

do_stuff(tonumber(pick_one()))