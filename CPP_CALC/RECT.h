#ifndef RECT_H_INCLUDED
#define RECT_H_INCLUDED

class rect : protected operation {
public:
	rect(float , float);
	rect(float);
	~rect();
	float area_r(void);
	float area_s(void);
	float perim_r(void);
	float perim_s(void);
};

#endif // RECT_H_INCLUDED