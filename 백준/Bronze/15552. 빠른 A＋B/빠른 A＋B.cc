#include <iostream>
#include <vector>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	vector<pair<int, int>> v(T);
	for (int i = 0; i < T; i++)
	{
		cin >> v[i].first >> v[i].second;
	}
	for (int i = 0; i < T; i++)
		cout << v[i].first + v[i].second << "\n";

	return 0;
}