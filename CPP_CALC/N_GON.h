#ifndef N_GON_H_INCLUDED
#define N_GON_H_INCLUDED

class n_gon : protected operation {
public:
	n_gon(float , float);
	~n_gon();
	float area_n(void);
	float area_p(void); 
};

#endif // N_GON_H_INCLUDED