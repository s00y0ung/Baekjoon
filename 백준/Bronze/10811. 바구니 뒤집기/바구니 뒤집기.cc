#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int N, M;
	int i, j;
	cin >> N >> M;

	int* arr = new int[N+1];
	for (int k = 0; k <= N; k++)
		arr[k] = k;

	for (int k = 0; k < M; k++)
	{
		cin >> i >> j;
		reverse(arr+i, arr+j+1);
	}

	for (int k = 1; k <= N; k++)
		cout << arr[k] << " ";

	return 0;
}