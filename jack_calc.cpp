#include <iostream>

#define PI 3.131592

class operation {
protected:
	float input1;
	float input2;
	float input3;
	float result;
	operation();
	operation(float);
	operation(float , float);
	operation(float , float , float);
};

class addition : protected operation {
public:
	addition(float , float);
	float adding(void);
};

class subtraction : protected operation {
public:	
	subtraction(float , float);
	float subbing(void);
};

class multiplication : protected operation {
public:
	multiplication(float , float);
	float multing(void);
};

class division : protected operation {
public:
	division(float , float);
	float divving(void);
};

float addition::adding()
{
	result = input1 + input2;
	return result;
}

float subtraction::subbing()
{
	result = input1 - input2;
	return result;
}

float multiplication::multing()
{
	result = input1 * input2;
	return result;
}

float division::divving()
{
	result = input1 / input2;
	return result;
}
