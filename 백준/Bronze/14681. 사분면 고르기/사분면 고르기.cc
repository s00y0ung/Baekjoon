#include <iostream>
using namespace std;

int main()
{
	int x, y;
	cin >> x;
	cin >> y;

	if (x > 0)
	{
		if (y > 0) cout << "1";
		if (y < 0) cout << "4";
	}
	else
	{
		if (y > 0) cout << "2";
		if (y < 0) cout << "3";
	}
}