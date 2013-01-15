#ifndef TRI_H_INCLUDED
#define TRI_H_INCLUDED

class tri : protected operation {
public:
	tri(float , float);
	~tri();
	float area_t(void);
	float perim_t(void);
};

#endif // REI_H_INCLUDED