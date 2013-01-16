#ifndef CIRCLE_H_INCLUDED
#define CIRCLE_H_INCLUDED

#define PI 3.14159265359
#define DEG_TO_RAD (PI / 180)

class circle : protected operation {
public:
	circle(float);
	circle(float , float);
	~circle();
	float area_c(void);
	float circum(void);
	float arc_length(void);
	float seg_area(void);
	float showi1(void);
	float showi2(void);

};

circle::circle(float i1)
{
	input1 = new float;
	*input1 = i1;
}

circle::circle(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

circle::~circle()
{
	delete input1;
	delete input2;
}

float circle::area_c(void)
{
	float a;
	a = PI * ((*input1) * (*input1));
	return a;
}

float circle::circum(void)
{
	float c;
	c = PI * 2 * (*input1);
	return c;
}

float circle::arc_length(void)
{
	float l;
	l = *input1 * *input2;
	return l;
}

float circle::seg_area(void) //i1 = theta , i2 = radius
{
	float a;
	float t_rad = (DEG_TO_RAD * *input1);
	a = (((*input2 * *input2) / 2) * ((t_rad) - sin(t_rad)));
	return a;
}

float circle ::showi1(void)
{
	return *input1;
}
float circle ::showi2(void)
{
	return *input2;
}

#endif // CIRCLE_H_INCLUDED