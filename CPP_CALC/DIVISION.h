#ifndef DIVISION_H_INCLUDED
#define DIVISION_H_INCLUDED

class division : protected operation {
public:
	division(float , float);
	~division();
	float divving(void);
};

division::division(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

division::~division()
{
	delete input1;
	delete input2;
}

float division::divving(void)
{
	float result;
	result = *input1 / *input2;
	return result;
}



#endif // DIVISION_H_INCLUDED