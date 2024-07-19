#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	int money = 0;

	if (a == b && b == c)
		money = 10000 + a * 1000;
	else if (a == b)
		money = 1000 + a * 100;
	else if (a == c)
		money = 1000 + a * 100;
	else if (c == b)
		money = 1000 + b * 100;
	else
	{
		int max = a > b ? a : b;
		max = max > c ? max : c;

		money = max * 100;
	}

	cout << money;
	

	return 0;
}