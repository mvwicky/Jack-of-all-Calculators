#ifndef OPERATION_H_INCLUDED
#define OPERATION_H_INCLUDED

class operation {
protected:
	float *input1;
	float *input2;
	float *input3;
	float *result;
public:
	operation();
	operation(float);
	operation(float , float);
	operation(float , float , float);
};

operation::operation()
{

}

operation::operation(float i1)
{
	input1 = new float;
	*input1 = i1;
}

operation::operation(float i1 , float i2)
{
	input1 = new float;
	input2 = new float;
	*input1 = i1;
	*input2 = i2;
}

operation::operation(float i1 , float i2 , float i3)
{	
	input1 = new float;
	input2 = new float;
	input3 = new float;
	*input1 = i1;
	*input2 = i2;
	*input3 = i3;
}



#endif // OPERATION_H_INCLUDED