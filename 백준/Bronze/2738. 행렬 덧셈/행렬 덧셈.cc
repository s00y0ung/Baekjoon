#include <iostream>
using namespace std;

int main()
{
	int N, M, v;
	cin >> N >> M;

	int** a = new int* [N];
	for (int i = 0; i < N; i++)
		a[i] = new int[M];
	
	int** b = new int* [N];
	for (int i = 0; i < N; i++)
		b[i] = new int[M];

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> v;
			a[i][j] = v;
		}
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> v;
			b[i][j] = v;
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cout << a[i][j]+b[i][j] << " ";
		}
		cout << "\n";
	}
	return 0;
}