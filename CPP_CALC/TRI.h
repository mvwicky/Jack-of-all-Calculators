#ifndef TRI_H_INCLUDED
#define TRI_H_INCLUDED

class tri : protected operation {
public:
	tri(float , float);
	~tri();
	float area_t(void);
	float perim_t(void);
	float showi1(void);
	float showi2(void);
};

#endif // REI_H_INCLUDED