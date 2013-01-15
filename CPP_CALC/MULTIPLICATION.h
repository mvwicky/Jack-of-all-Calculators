#ifndef MULTIPLICATION_H_INCLUDED
#define MULTIPLICATION_H_INCLUDED

class multiplication : protected operation {
public:
	multiplication(float , float);
	~multiplication();
	float multing(void);
};

multiplication::multiplication(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

multiplication::~multiplication()
{
	delete input1;
	delete input2;
}

float multiplication::multing(void)
{
	float result;
	result = *input1 * *input2;
	return result;
}


#endif // MULTIPLICATION_H_INCLUDED