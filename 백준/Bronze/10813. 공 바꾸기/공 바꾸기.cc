#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N, M;
	int i, j, temp;

	cin >> N >> M;

	vector<int> v(N+1);
	for (int k = 0; k <= N; k++)
		v[k] = k;
	for (int k = 0; k < M; k++)
	{
		cin >> i >> j;
		temp = v[i];
		v[i] = v[j];
		v[j] = temp;
	}

	for (int x = 1; x <= N; x++)
		cout << v[x] << " ";

	return 0;
}