#ifndef RECT_H_INCLUDED
#define RECT_H_INCLUDED

class rect : protected operation {
public:
	rect(float , float);
	~rect();
	float area_r(void);
	float area_s(void);
	float perim_r(void);
	float perim_s(void);
	float showi1(void);
	float showi2(void);


};

rect::rect(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

rect::~rect()
{
	delete input1;
	delete input2;
}

float rect::area_r(void)
{
	float area;
	area = *input1 * *input2;
	return area;

}

float rect::perim_r(void)
{
	float perim;
	perim = (2 * *input1) + (2 * *input2);
	return perim;
}

float rect::showi1(void)
{
	return *input1;
}
float rect::showi2(void)
{
	return *input2;
}

class square : protected operation {
public:
	square(float);
	~square();
	float area_s(void);
	float perim_s(void);
	float showi1(void);
};

square::square(float i1)
{
	input1 = new float;
	*input1 = i1;
}

square::~square()
{
	delete input1;
}

float square::area_s(void)
{
	float area;
	area = *input1 * *input1;
	return area;
}

float square::perim_s(void)
{
	float perim;
	perim = (4 * *input1);
	return perim;
}

float square::showi1(void)
{
	return *input1;
}

#endif // RECT_H_INCLUDED