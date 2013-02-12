class conversion {
protected:
	int *wu;
	int *to;
	float *starting;
	float *result;
	float *len;
	float *mass;
public:
	static float len_u[4][4]; 
	static float mass_u[7][8]; 

	conversion(int , int , float , float);
	~conversion();
};

conversion::conversion(int w , int t , float s , float r)
{
	wu = new int;
	to = new int;
	starting = new float;
	result = new float;
	len = new float [20];
	mass = new float [56];
	*wu = w;
	*to = t;
	*starting = s;
	*result = r;
	*len[] = *len_u;
	*mass[] = *mass_u;
}

conversion::~conversion()
{
	delete wu;
	delete to;
	delete starting;
	delete result;
	delete len;
	delete mass;
}