#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N, M;
	int i, j, k;
	cin >> N >> M;

	vector<int> v(N+1,0);
	for (int x = 0; x < M; x++)
	{
		cin >> i >> j >> k;
		for (int q = i; q <= j; q++)
			v[q] = k;
	}

	for (int x = 1; x <= N; x++)
		cout << v[x] << " ";

	return 0;
}