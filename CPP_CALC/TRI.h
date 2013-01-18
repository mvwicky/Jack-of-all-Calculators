#ifndef TRI_H_INCLUDED
#define TRI_H_INCLUDED

class tri : protected operation {
private:
	bool isini;
public:
	tri(float , float);
	tri(float , float , float);
	~tri();
	float area_t(void);
	float perim_t(void);
	float showi1(void);
	float showi2(void);
	float showi3(void);
};

tri::tri(float b , float h)
{
	input1 = new float;
	input2 = new float;
	isini = false;
	*input1 = b;
	*input2 = h;
}

tri::tri(float s1 , float s2 , float s3)
{
	input1 = new float;
	input2 = new float;
	input3 = new float;
	isini = true;
	*input1 = s1;
	*input2 = s2;
	*input3 = s3;
}

tri::~tri()
{
	delete input1;
	delete input2;
	if (isini == true)
	{
		delete input3;
	}
}

float tri::area_t(void)
{
	float a;
	a = ((*input1 * *input2) / 2);
	return a;
}

float tri::perim_t(void)
{
	float p;
	bool case1 = true;
	bool case2 = true;
	bool case3 = true;
	if (*input1 >= *input2 + *input3)
		case1 = false;
	if (*input2 >= *input1 + *input3)
		case2 = false;
	if (*input3 >= *input1 + *input2)
		case3 = false;
	if(case1 == true && case2 == true && case3 == true)
	{
		p = *input1 + *input2 + *input3;
		return p;
	}
	else
		return -1;
}

float tri::showi1(void)
{
	return *input1;
}
float tri::showi2(void)
{
	return *input2;
}

float tri::showi3(void)
{
	return *input3;
}
#endif // REI_H_INCLUDED