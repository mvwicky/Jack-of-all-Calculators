#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int enemies = 1;

int strike(int slevel);
int defend(int dlevel);
int gEvent();
void setupMe();
void setupEnemy();
bool stay();

struct character {
	int level;
	int expe;
	int health;
	int strength;
	int defence;
}me , enemy[100];

int main()
{
	srand(time(NULL));
	setupMe();
	//int to_me;
	int from_me;
	bool in = true;
	string w;
	while (in == true)
	{
		cout << "w" << endl;
		cin >> w;
		setupEnemy();

		cout << "watch out!, an enemy!";
		cout << "Enemy has " << enemy[enemies].health << "health" << endl; 
		cin.ignore();
		while (enemy[enemies].health >= 0)
		{
			from_me = strike(me.strength) - defend(enemy[enemies].defence);
			enemy[enemies].health = enemy[enemies].health - from_me; 
			cout << "You deal " << from_me << " damage" << endl;
			cout << "Enemy has " << enemy[enemies].health << "health left" << endl;
			cin.ignore();
			if (enemy[enemies].health == 0)
				break;
		}
		in = stay();
	}
	return 0;
}


int strike(int slevel)
{
	int hit;
	hit = (rand() % (slevel + 1));
	return hit;
}

int defend(int dlevel)
{
	int def;
	def = (rand() % (dlevel + 1));
	return def;
}

int gEvent()
{
	bool ev;
	int rnum;
	rnum = (rand() % 2);
	if (rnum == 1)
		ev = true;
	if (rnum == 0)
		ev = false;
	return ev;
}

void setupMe()
{
	me.level = 1;
	me.expe = 0;
	me.health = 15;
	me.strength = 3;
	me.defence = 3;
}

void setupEnemy()
{
	enemies += 1;
	enemy[enemies].level = (rand() % me.level);
	enemy[enemies].expe = 0;
	enemy[enemies].health = 15;
	enemy[enemies].strength = (rand() % me.level);
	enemy[enemies].defence = (rand() % me.defence);
	cout << enemy[enemies].level << endl;
	cout << enemy[enemies].expe << endl;
	cout << enemy[enemies].health << endl;
	cout << enemy[enemies].strength << endl;
	cout << enemy[enemies].defence << endl;

	
}

bool stay()
{
	string collect;
	cout << "Stay In?";
	cout << "Y or N" << endl;
	cin >> collect;
	if (collect == "Y" || collect == "y")
		return true;
	if (collect == "N" || collect == "n")
		return false;
	else
		return true;
}