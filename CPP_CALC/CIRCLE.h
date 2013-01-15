#ifndef CIRCLE_H_INCLUDED
#define CIRCLE_H_INCLUDED

class circle : protected operation {
public:
	circle(float);
	circle(float , float);
	~circle();
	float area_c(void);
	float circum(void);
	float arc_length(void);
	float seg_area(void);
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

#endif // CIRCLE_H_INCLUDED