#ifndef ADDITION_H_INCLUDED
#define ADDITION_H_INCLUDED

class addition : protected operation {
public:
	addition(float , float);
	~addition();
	float adding(void);
};

addition::addition(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

addition::~addition()
{
	delete input1;
	delete input2;
}

float addition::adding(void)
{
	float result;
	result = *input1 + *input2;
	return result;
}

#endif // ADDITION_H_INCLUDED