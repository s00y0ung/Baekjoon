#include <iostream>
using namespace std;

int main()
{
	int h, m, tt;

	cin >> h >> m;
	cin >> tt;

	int time = h * 60 + m;
	time += tt;

	if (time >= 60 * 24)
		time -= 60 * 24;
	cout << time / 60 << " " << time % 60;

	return 0;
}