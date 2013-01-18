#ifndef EXPONENTATION_H_INCLUDED
#define EPONENTATION_H_INCLUDED
#include <math.h>

class exponentation : protected operation {
public:
	exponentation(float , float);
	~exponentation();
	float expping(void);
	float showi1(void);
	float showi2(void);
};

exponentation::exponentation(float b , float p)
{
	input1 = new float;
	input2 = new float;
	*input1 = b;
	*input2 = p;
}

exponentation::~exponentation()
{
	delete input1;
	delete input2;
}

float exponentation::expping(void)
{
	float result;
	result = pow(*input1 , *input2);
	return result;
}

float exponentation::showi1(void)
{
	return *input1;
}
float exponentation::showi2(void)
{
	return *input2;
}

#endif // EXPONENTATION_H_INCLUDED