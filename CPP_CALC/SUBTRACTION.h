#ifndef SUBTRACTION_H_INCLUDED
#define SUBTRACTION_H_INCLUDED

class subtraction : protected operation {
public:	
	subtraction(float , float);
	~subtraction();
	float subbing(void);
};

subtraction::subtraction(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

subtraction::~subtraction()
{
	delete input1;
	delete input2;
}

float subtraction::subbing(void)
{
	float result;
	result = *input1 - *input2;
	return result;
}


#endif // SUBTRACTION_H_INCLUDED