#include <iostream>

#define PI 3.131592

class operation {
protected:
	float *input1;
	float *input2;
	float *input3;
	float *result;
	operation();
	operation(float);
	operation(float , float);
	operation(float , float , float);
	//~operation();
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

operation::operation(float i1)
{
	input1 = new float;
	*input1 = i1;
}

operation::operation(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

operation::operation(float i1 , float i2 , float i3)
{
	input1 = new float;
	input2 = new float;
	input3 = new float;
	*input1 = i1;
	*input2 = i2;
	*input3 = i3;

}

addition::addition(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

float addition::adding()
{
	*result = *input1 + *input2;
	return *result;
}

subtraction::subtraction(float i1 , float i1)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

float subtraction::subbing()
{
	*result = *input1 - *input2;
	return *result;
}

multiplication::multiplication(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

float multiplication::multing()
{
	*result = *input1 * *input2;
	return *result;
}

division::division(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

float division::divving()
{
	*result = *input1 / *input2;
	return *result;
}
