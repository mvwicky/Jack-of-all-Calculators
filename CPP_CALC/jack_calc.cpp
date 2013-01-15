#include <iostream>
#include <string.h>
#include "OPERATION.h"
#include "ADDITION.h"
#include "SUBTRACTION.h"
#include "MULTIPLICATION.h"
#include "DIVISION.h"

#define PI 3.131592


//string ops[] = {" + " , " - " , " * " , " / "};


using namespace std;

int make_menu();
float do_op(int w);

int main()
{
	do_op(make_menu());
	
}

int make_menu()
{
	int wop;
	cout << "1. Addition" << endl;
	cout << "2. Subtraction" << endl;
	cout << "3. Multiplication" << endl;
	cout << "4. Division" << endl;
	cin>>wop;
	return wop;
}

float do_op(int w)
{
	float opin1;
	float opin2;
	switch (w)
	{
		case 1:
		{
			cout << "Input 1 = " << endl;
			cin >> opin1;
			cout << "Input 2 = " << endl;
			cin >> opin2;
			addition add (opin1 , opin2);
			cout << opin1 << " + " << opin2 << " = " << add.adding() << endl;
			add.~addition();
			break;
		}
		case 2:
		{
			cout << "Input 1 = " << endl;
			cin >> opin1;
			cout << "Input 2 = " << endl;
			cin >> opin2;
			subtraction sub (opin1 , opin2);
			cout << opin1 << " - " << opin2 << " = " << sub.subbing() << endl;
			sub.~subtraction();
			break;
		}
		case 3:
		{
			cout << "Input 1 = " << endl;
			cin >> opin1;
			cout << "Input 2 = " << endl;
			cin >> opin2;
			multiplication mult (opin1 , opin2);
			cout << opin1 << " * " << opin2 << " = " << mult.multing() << endl;
			mult.~multiplication();
			break;
		}
		case 4:
		{
			cout << "Input 1 = " << endl;
			cin >> opin1;
			cout << "Input 2 = " << endl;
			cin >> opin2;
			division divs (opin1 , opin2);
			cout << opin1 << " / " << opin2 << " = " << divs.divving() << endl;
			divs.~division();
			break;
		}

	}
	return 0;
}
