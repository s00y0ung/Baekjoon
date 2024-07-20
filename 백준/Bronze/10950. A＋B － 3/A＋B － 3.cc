#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int cnt;
	cin >> cnt;

	vector<pair<int,int>> V(cnt);
	for (int i = 0; i < cnt; i++)
	{
		cin >> V[i].first >> V[i].second;
	}

	for (int i = 0; i < cnt; i++)
	{
		cout << V[i].first + V[i].second << "\n";
	}

	return 0;
}