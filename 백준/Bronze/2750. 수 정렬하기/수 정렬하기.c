#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define SWAP(x,y,t) ((t)=(x), (x)=(y), (y)=(t))

void bubbleSort(int* arr, int N)
{
	int tmp;
	for (int i = N - 1; i > 0; i--)
	{
		for (int j = 0; j < i; j++)
		{
			if (arr[j] > arr[j + 1])
				SWAP(arr[j], arr[j + 1], tmp);
		}
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	int arr[1000];
	for (int i = 0; i < N; i++)
		scanf("%d", arr + i);

	bubbleSort(arr, N);
	for (int i = 0; i < N; i++)
		printf("%d\n", arr[i]);

	return 0;
}