-- JACK_CALC Lua
--[[
TODO-Make a function that takes in inputs to a table. 
	-Make a function that reads those inputs back into a operator function
	]]--
--base function definitions
function addition(...)
	local ag = table.getn(arg) -- number of args
	local n = 1
	local sum = 0
	while (n <= ag)
		do
		sum = sum + arg[n]
		n = n + 1
	end
	print(sum) 
end

function subtraction(...)
	local ag = table.getn(arg) -- number of args
	local n = 1
	local diff = 0
	while (n <= ag)
		do
		diff = diff - arg[n]
		n = n + 1
	end
	print(diff) 
end
 
function multiplication(...)
	local ag = table.getn(arg) -- number of args
	local n = 1
	local prod = 1
	while (n <= ag)
		do
		prod = prod * arg[n]
		n = n + 1
	end
	print(prod)
end

function division(...)
	local ag = table.getn(arg) -- number of args
	local n = 1
	local quot = 1 
	while (n <= ag)
		do
		quot = quot / arg[n]
		n = n + 1
	end
	print(quot)
end

