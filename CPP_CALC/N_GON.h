#ifndef N_GON_H_INCLUDED
#define N_GON_H_INCLUDED

class n_gon : protected operation {
public:
	n_gon(float , float);
	~n_gon();
	float area_n(void);
	float perim_n(void); 
	float showi1(void);
	float showi2(void);
};

n_gon::n_gon(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

n_gon::~ngon()
{
	delete input1;
	delete input2;
}

float n_gon::area_n(void)
{
	float area;
	area = (.25 * (*input1 * (*input2 * *input2)) * (1 / tan(PI / *input1)))
	return area;
}

float n_gon::perim_n(void)
{
	float perim;
	perim = *input1 * *input2;
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

#endif // N_GON_H_INCLUDED