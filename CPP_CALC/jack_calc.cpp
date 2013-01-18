#include <iostream>
#include <string.h>
#include <math.h>
#include "OPERATION.h"
#include "ADDITION.h"
#include "SUBTRACTION.h"
#include "MULTIPLICATION.h"
#include "DIVISION.h"
#include "CIRCLE.h"
#include "RECT.h"
#include "EXPONENTATION.h"
#include "TRI.h"

#define PI 3.14159265359
#define DEG_TO_RAD (PI / 180)


//string ops[] = {" + " , " - " , " * " , " / "};


using namespace std;

int make_menu();
float do_op(int w);
int rect_menu();
void do_rect(int wr);
int circ_menu();
void do_circ(int wc);
int tri_menu();
void do_tri(int wt);

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
	cout << "5. Exponentation" << endl;
	cout << "6. Rectangles" << endl;
	cout << "7. Circles" << endl;
	cout << "8. Triangles" << endl;
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
			//add.~addition();
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
			//sub.~subtraction();
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
			//mult.~multiplication();
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
			//divs.~division();
			break;
		}
		case 5:
		{
			cout << "Base = " << endl;
			cin >> opin1;
			cout << "Power = " << endl;
			cin >> opin2;
			exponentation exps (opin1 , opin2);
			cout << opin1 << " ^ " << opin2 << " = " << exps.expping() << endl;
			//divs.~division();
			break;
		}
		case 6:
		{
			do_rect(rect_menu());
			break;
		}
		case 7:
		{
			do_circ(circ_menu());
			break;
		}
		case 8: 
		{
			do_tri(tri_menu());
			break;
		}
	}
	return 0;
}
 
int rect_menu()
{	
	int wrect;
	cout << "1. Perimeter of a Square" << endl;
	cout << "2. Perimeter of a Rectangle" << endl;
	cout << "3. Area of a Square" << endl;
	cout << "4. Area of a Rectangle" << endl;
	cin >> wrect;
	return wrect;
}

void do_rect(int wr)
{
	float side1;
	float side2;
	switch (wr)
	{
		case 1:
		{	
			cout << "Side Length:" << endl;
			cin >> side1;			
			square sqp(side1);
			cout << "4 " << " * " << sqp.showi1() << " = " << sqp.perim_s() << endl;	
			break;
		}
		case 2:
		{
			cout << "Side 1 Length" << endl;
			cin >> side1;
			cout << "Side 2 Length" << endl;
			cin >> side2;
			rect rep(side1 , side2);
			cout << "2 * " << rep.showi1() << " + " << "2 * " << rep.showi2() << " = " << rep.perim_r() << endl;
			break;
		}	
		case 3:
		{
			cout << "Side Length" << endl;
			cin >> side1;
			square sqa(side1);
			cout << sqa.showi1() << " * " << sqa.showi1() << " = " << sqa.area_s() << endl;
			break;
		}
		case 4:
		{
			cout << "Side 1 Length" << endl;
			cin >> side1;
			cout << "Side 2 Length" << endl;
			cin >> side2;
			rect rea(side1 , side2);
			cout << rea.showi1() << " * " << rea.showi2() << " = " << rea.area_r() << endl;
			break;
		}
	}
}

int circ_menu()
{	
	int wcirc;
	cout << "1. Circumference of a Circle" << endl;
	cout << "2. Area of a Circle" << endl;
	cout << "3. Arc Length" << endl;
	cout << "4. Segment Area" << endl;
	cin >> wcirc;
	return wcirc;
}

void do_circ(int wc)
{
	float one;
	float two;
	switch (wc)
	{
		case 1: // circumference
		{
			cout << "Radius:" << endl;
			cin >> one;
			circle ccirc(one);
			cout << "(2 * " << ccirc.showi1() << ") * " << PI << " = " << ccirc.circum() << endl;
			break;
		}
		case 2: // Area
		{
			cout  << "Radius:" << endl;
			cin >> one;
			circle acirc(one);
			cout << PI << " * (" << acirc.showi1() << "^2)" <<  " = " << acirc.area_c() << endl;
			break;
		}
		case 3: // Arc Length
		{

			cout << "Angle in Degrees:" << endl;
			cin >> two;
			cout << "Radius:" << endl;
			cin >> one;
			circle arccirc(one , two);
			cout << arccirc.showi1() << " * (" << (arccirc.showi2() * DEG_TO_RAD) << ") = " << arccirc.arc_length() << endl;
			break;
		}
		case 4: // Segment Area
		{
			cout << "Angle in Degress:" << endl;
			cin >> one;
			cout << "Radius:" << endl;
			cin >> two;
			circle segcirc(one , two);
			cout << segcirc.seg_area() << endl;
			break;
		}
	}
}

int tri_menu()
{	
	int wtri;
	cout << "1. Perimeter of a Triangle" << endl;
	cout << "2. Area of a Triangle" << endl;
	cin >> wtri;
	return wtri;
}

void do_tri(int wt)
{
	float s1; // base
	float s2; // height
	float s3;
	switch (wt)
	{
		case 1:
		{
			cout << "Side 1:" << endl;
			cin >> s1;
			cout << "Side 2:" << endl;
			cin >> s2; 
			cout << "Side 3:" << endl;
			cin >> s3;
			tri ptri(s1 , s2 , s3);
			if (ptri.perim_t() == -1)
			{
				cout << "Not a Valid Triangle" << endl;
			}
			else
				cout << ptri.showi1() << " + " << ptri.showi2() << " + " << ptri.showi3() << " = " << ptri.perim_t() << endl;
			break;
		}
		case 2:
		{
			cout << "Base:" << endl;
			cin >> s1;
			cout << "Height:" << endl;
			cin >> s2;
			tri atri(s1 , s2);
			cout << "(" << atri.showi1() << " * " << atri.showi2() << ") / 2 = " << atri.area_t() << endl; 
			break;
		}
	}
}