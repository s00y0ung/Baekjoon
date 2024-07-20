#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int i = 0;

	pair<int, int> p;
	cin >> p.first >> p.second;
	
	vector<pair<int, int>> v;

	while (p.first != 0 && p.second != 0)
	{
		v.push_back(p);
		cin >> p.first >> p.second;
	}

	for (int i = 0; i < v.size(); i++)
		cout << v[i].first + v[i].second << "\n";
	return 0;
}