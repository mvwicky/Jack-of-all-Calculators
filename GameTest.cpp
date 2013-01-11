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
	bool in = true;
	while (in == true)
	{
		string fward;
		cout << "w" << endl;
		cin >> fward;
		in = stay();
	}
	return 0;
}


int strike(int slevel)
{
	int hit;
	srand(time(NULL));
	hit = (rand() % (slevel + 1));
	return hit;
}

int defend(int dlevel)
{
	int def;
	srand(time(NULL));
	def = (rand() % (dlevel + 1));
	return def;
}

int gEvent()
{
	bool ev;
	int rnum;
	srand(time(NULL));
	rnum = (rand() % 2);
	if (rnum == 1)
		ev = true;
	else
		ev = false;
	return ev;
}

void setupMe()
{
	me.level = 1;
	me.expe = 0;
	me.health = 15;
	me.strength = 1;
	me.defence = 1;
}

void setupEnemy()
{
	srand(time(NULL));
	enemy[enemies].level = (rand() % me.level);
	enemy[enemies].expe = 0;
	enemy[enemies].health = (rand() % me.health);
	enemy[enemies].strength = (rand() % me.level);
	enemy[enemies].defence = (rand() % me.defence);
	enemies += 1;
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